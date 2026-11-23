#!/usr/bin/env python3
"""Add or verify source-pinned model snapshots without contacting a service.

plan/apply require an external JSON source map: {source_key: original_checkout}.
Source machine paths are deliberately not stored in the public manifest.
verify is offline unless --check-source is specified. No vendor code is run.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import tempfile


REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "docs/platform-import/manifest.json"
BAD_PARTS = {".git", "pex", "rcx", "qrc", "psf", "__pycache__"}
BAD_EXTENSIONS = {".gds", ".gdsii", ".lef", ".oa", ".cdl", ".dspf", ".spef", ".tr0", ".raw"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def relative(value):
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError("Unsafe relative path: " + repr(value))
    return path


def bounded(root, value, destination=False):
    parts = relative(value).parts
    path = root.joinpath(*parts)
    if destination:
        cursor = root
        for part in parts:
            cursor = cursor / part
            if cursor.is_symlink():
                raise ValueError("Destination symlink: " + str(cursor))
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError("Path escapes root: " + str(path)) from exc
    return path


def load_manifest(path):
    data = json.loads(path.read_text())
    if data["schema_version"] != "spice.platform-import.v1":
        raise ValueError("Unsupported model manifest")
    if data["repo_kind"] not in {"public", "private"}:
        raise ValueError("Unknown repository kind")
    bundles = {b["id"]: b for b in data["bundles"]}
    paths = set()
    for item in data["files"]:
        parts = relative(item["path"]).parts
        relative(item["upstream_path"])
        if data["repo_kind"] == "private":
            safe = len(parts) >= 4 and parts[0] == "private-models" and parts[2].startswith("platform_")
        else:
            safe = (len(parts) >= 3 and parts[0] not in {"private-models", "public-models", "docs", "scripts", ".github"}
                    and parts[1].startswith("platform_"))
        if not safe or BAD_PARTS.intersection(p.lower() for p in parts) or PurePosixPath(item["path"]).suffix.lower() in BAD_EXTENSIONS:
            raise ValueError("Out-of-scope model destination: " + item["path"])
        if item["path"] in paths:
            raise ValueError("Duplicate destination: " + item["path"])
        paths.add(item["path"])
        bundle = bundles[item["bundle_id"]]
        if data["repo_kind"] == "public" and not bundle.get("public_distribution"):
            raise ValueError("Public redistribution review missing: " + bundle["id"])
        if len(item["sha256"]) != 64 or any(c not in "0123456789abcdef" for c in item["sha256"]):
            raise ValueError("Invalid SHA-256: " + item["path"])
        if not 0 <= item["size"] < 2 * 1024 * 1024 * 1024 or item["mode"] not in {"0644", "0755"}:
            raise ValueError("Invalid size/mode: " + item["path"])
        if item.get("storage", "git") not in {"git", "git-lfs"}:
            raise ValueError("Invalid storage mode")
        if item["size"] >= 100 * 1024 * 1024 and item.get("storage") != "git-lfs":
            raise ValueError("Large files must use Git LFS: " + item["path"])
    return data


def checked_bytes(root, value, item, destination=False):
    path = bounded(root, value, destination)
    if not path.is_file():
        raise ValueError("Missing regular file: " + str(path))
    content = path.read_bytes()
    if len(content) != item["size"] or digest(content) != item["sha256"]:
        raise ValueError("Content changed: " + str(path))
    return content


def source_bytes(item, source_map):
    if item["source_key"] not in source_map:
        raise ValueError("Source map key missing: " + item["source_key"])
    return checked_bytes(Path(source_map[item["source_key"]]), item["upstream_path"], item)


def preflight(manifest, root, source_map, check_source, require_dest):
    new = unchanged = 0
    for item in manifest["files"]:
        dest = bounded(root, item["path"], True)
        if check_source:
            source_bytes(item, source_map)
        if dest.exists():
            checked_bytes(root, item["path"], item, True)
            if bool(dest.stat().st_mode & 0o111) != (item["mode"] == "0755"):
                raise ValueError("Executable mode changed: " + str(dest))
            unchanged += 1
        elif require_dest:
            raise ValueError("Missing destination: " + str(dest))
        else:
            new += 1
    return {"files": len(manifest["files"]), "new": new, "unchanged": unchanged,
            "bytes": sum(x["size"] for x in manifest["files"])}


def apply(manifest, root, source_map):
    summary = preflight(manifest, root, source_map, True, False)
    for item in manifest["files"]:
        dest = bounded(root, item["path"], True)
        if dest.exists():
            checked_bytes(root, item["path"], item, True)
            continue
        content = source_bytes(item, source_map)
        dest.parent.mkdir(parents=True, exist_ok=True)
        bounded(root, item["path"], True)
        fd, temporary = tempfile.mkstemp(prefix=".model-import-", dir=dest.parent)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
                os.fchmod(stream.fileno(), int(item["mode"], 8))
            os.link(temporary, dest)  # Atomic, refuses an existing destination.
        finally:
            os.unlink(temporary)
    preflight(manifest, root, source_map, False, True)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("plan", "apply", "verify"))
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--repo-root", type=Path, default=REPO)
    parser.add_argument("--source-map", type=Path)
    parser.add_argument("--check-source", action="store_true")
    args = parser.parse_args()
    source_map = json.loads(args.source_map.read_text()) if args.source_map else {}
    manifest = load_manifest(args.manifest)
    if not args.repo_root.is_dir():
        raise ValueError("Repository root must already exist")
    if args.command == "apply":
        result = apply(manifest, args.repo_root.resolve(), source_map)
    else:
        result = preflight(manifest, args.repo_root.resolve(), source_map,
                           args.command == "plan" or args.check_source, args.command == "verify")
    print(json.dumps({"status": "passed", "command": args.command, **result}, sort_keys=True))


if __name__ == "__main__":
    main()
