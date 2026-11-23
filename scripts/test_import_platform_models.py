"""Import safety tests use isolated synthetic files, never a real PDK."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("models", Path(__file__).with_name("import_platform_models.py"))
models = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(models)


class ImportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source, self.repo = self.base / "source", self.base / "repo"
        self.source.mkdir()
        self.repo.mkdir()
        self.content = b"* synthetic\n.model tiny nmos level=1\n"
        (self.source / "tiny.lib").write_bytes(self.content)
        self.item = {"bundle_id": "tiny/v1", "source_key": "fixture", "upstream_path": "tiny.lib",
                     "path": "tiny/platform_v1/tiny.lib", "sha256": models.digest(self.content),
                     "size": len(self.content), "mode": "0644"}
        self.data = {"schema_version": "spice.platform-import.v1", "repo_kind": "public",
                     "bundles": [{"id": "tiny/v1", "public_distribution": {"license": "fixture"}}],
                     "files": [self.item]}
        self.mapping = {"fixture": str(self.source)}

    def load(self, data):
        path = self.base / "manifest.json"
        path.write_text(json.dumps(data))
        return models.load_manifest(path)

    def test_repeat_and_offline_verification(self):
        self.load(self.data)
        self.assertEqual(models.apply(self.data, self.repo, self.mapping)["new"], 1)
        self.assertEqual(models.apply(self.data, self.repo, self.mapping)["new"], 0)
        (self.source / "tiny.lib").unlink()
        self.assertEqual(models.preflight(self.data, self.repo, {}, False, True)["unchanged"], 1)

    def test_preflight_all_sources_before_any_copy(self):
        bad = copy.deepcopy(self.item)
        bad.update(upstream_path="missing.lib", path="tiny/platform_v1/missing.lib")
        self.data["files"].append(bad)
        with self.assertRaisesRegex(ValueError, "Missing regular file"):
            models.apply(self.data, self.repo, self.mapping)
        self.assertEqual(list(self.repo.iterdir()), [])

    def test_source_mutation_rejected(self):
        (self.source / "tiny.lib").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "Content changed"):
            models.apply(self.data, self.repo, self.mapping)

    def test_conflict_preserves_user_file(self):
        target = self.repo / self.item["path"]
        target.parent.mkdir(parents=True)
        target.write_text("user changes")
        with self.assertRaisesRegex(ValueError, "Content changed"):
            models.apply(self.data, self.repo, self.mapping)
        self.assertEqual(target.read_text(), "user changes")

    def test_manifest_path_and_scope_guards(self):
        for value in ("../escape", "/absolute", "tiny/platform_v1/../escape", "private-models/tiny/platform_v1/tiny.lib", "tiny/platform_v1/pex/rules", "tiny/platform_v1/layout.gds"):
            with self.subTest(value=value):
                data = copy.deepcopy(self.data)
                data["files"][0]["path"] = value
                with self.assertRaises(ValueError):
                    self.load(data)

    def test_duplicate_paths_rejected(self):
        self.data["files"].append(copy.deepcopy(self.item))
        with self.assertRaisesRegex(ValueError, "Duplicate destination"):
            self.load(self.data)

    def test_destination_symlink_rejected(self):
        (self.repo / "tiny").symlink_to(self.source, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Destination symlink"):
            models.apply(self.data, self.repo, self.mapping)

    def test_source_boundary_and_missing_mapping(self):
        with self.assertRaisesRegex(ValueError, "Source map key missing"):
            models.apply(self.data, self.repo, {})
        path = self.source / "tiny.lib"
        path.unlink()
        outside = self.base / "outside.lib"
        outside.write_bytes(self.content)
        path.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "Path escapes root"):
            models.apply(self.data, self.repo, self.mapping)

    def test_large_files_require_explicit_lfs_storage(self):
        self.item["size"] = 100 * 1024 * 1024
        with self.assertRaisesRegex(ValueError, "Large files must use Git LFS"):
            self.load(self.data)
        self.item["storage"] = "git-lfs"
        self.load(self.data)

    def test_public_redistribution_metadata_required(self):
        self.data["bundles"][0].pop("public_distribution")
        with self.assertRaisesRegex(ValueError, "Public redistribution review missing"):
            self.load(self.data)


if __name__ == "__main__":
    unittest.main()
