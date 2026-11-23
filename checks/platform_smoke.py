#!/usr/bin/env python3
"""Run bounded DC checks against the exported GF180, SKY130 and IHP models.

Uses a clean ngspice startup and an unused directory outside the checkout.
Checks actual finite, varying current data, not only the simulator exit code.
Includes intentional missing-model and missing-section failures.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def simulate(name, model_dir, deck, analysis, currents, out, binary, expect_failure=False):
    work = out / name
    work.mkdir()
    circuit = work / "circuit.cir"
    circuit.write_text(deck)
    driver = work / "driver.cir"
    driver.write_text("""Source-pinned library DC smoke
.control
set ngbehavior=hs
set sourcepath = ( . "%s" )
source circuit.cir
%s
wrdata currents.txt %s
quit
.endc
.end
""" % (model_dir, analysis, " ".join("i(%s)" % x for x in currents)))
    run = subprocess.run([binary, "-n", "-b", "driver.cir"], cwd=work,
                         capture_output=True, text=True, timeout=60)
    log = run.stdout + "\n" + run.stderr
    (work / "run.log").write_text(log)
    path = work / "currents.txt"
    if expect_failure:
        if path.exists() or not any(word in log.lower() for word in ("error", "unknown", "not found", "could not", "can't find")):
            raise RuntimeError(name + ": intentionally invalid input was not rejected")
        return {"case": name, "status": "passed", "expected_failure": True,
                "returncode": run.returncode, "deck_sha256": sha(circuit.read_bytes()),
                "log_sha256": sha(log.encode())}
    if run.returncode or not path.exists():
        raise RuntimeError(name + " failed; see " + str(work / "run.log"))
    rows = [[float(v) for v in line.split()] for line in path.read_text().splitlines()]
    if len(rows) < 10 or any(not math.isfinite(v) for row in rows for v in row):
        raise RuntimeError(name + ": missing or nonfinite DC data")
    values = {}
    for i, current in enumerate(currents):
        column = [row[2 * i + 1] for row in rows]
        if max(abs(v) for v in column) <= 1e-9 or max(column) - min(column) <= 1e-9:
            raise RuntimeError(name + ": current did not respond to input sweep")
        values[current] = {"first_A": column[0], "last_A": column[-1]}
    return {"case": name, "status": "passed", "points": len(rows), "currents": values,
            "returncode": run.returncode, "deck_sha256": sha(circuit.read_bytes()),
            "data_sha256": sha(path.read_bytes()), "log_sha256": sha(log.encode())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--ngspice-bin", default="ngspice")
    args = parser.parse_args()
    out = args.output.resolve()
    if out == ROOT or ROOT in out.parents:
        raise ValueError("Output must be outside this checkout")
    out.mkdir(parents=True, exist_ok=False)
    manifest = json.loads((ROOT / "docs/platform-import/manifest.json").read_text())
    gf = next(b for b in manifest["bundles"] if "gf180mcu" in b["pdk_ids"])
    sky = next(b for b in manifest["bundles"] if "sky130" in b["pdk_ids"])
    ihp = next(b for b in manifest["bundles"] if "ihp-sg13cmos5l" in b["pdk_ids"])
    checks = []
    gf_dir = ROOT / gf["directory"] / "ngspice"
    for device, voltage, length in (("3p3", 3.3, "0.5u"), ("6p0", 6.0, "0.8u")):
        deck = """GF180 exported model NMOS/PMOS DC check
.include design.ngspice
.lib sm141064.ngspice typical
.param sw_stat_global=0 sw_stat_mismatch=0
.temp 27
Vg g 0 0
Vn dn 0 1
Vp dp 0 %s
Vdd vdd 0 %s
Xn dn g 0 0 nmos_%s w=10u l=%s
Xp dp g vdd vdd pmos_%s w=10u l=%s
.end
""" % (voltage - 1, voltage, device, length, device, length)
        checks.append(simulate("gf180_" + device, gf_dir, deck,
                               "dc Vg 0 %s %s" % (voltage, voltage / 10),
                               ("Vn", "Vp"), out, args.ngspice_bin))
        if device == "3p3":
            for name, broken in (("missing_model", deck.replace("nmos_3p3", "model_deliberately_missing")),
                                 ("missing_section", deck.replace("ngspice typical", "ngspice section_deliberately_missing"))):
                checks.append(simulate(name, gf_dir, broken, "dc Vg 0 3.3 0.33",
                                       ("Vn", "Vp"), out, args.ngspice_bin, True))
    sky_dir = ROOT / sky["directory"]
    profile = next(x["profile"] for x in sky["profiles"] if x["profile"]["engine"] == "ngspice")
    loads = "\n".join('.include "%s"' % x["path"] for x in profile["loads"])
    deck = """SKY130 exported 1.8 V core pair DC check
%s
.option scale=1e-6
.temp 27
Vg g 0 0
Vn dn 0 0.9
Vp dp 0 0.9
Vdd vdd 0 1.8
Xn dn g 0 0 sky130_fd_pr__nfet_01v8 w=1 l=0.15
Xp dp g vdd vdd sky130_fd_pr__pfet_01v8 w=2 l=0.15
.end
""" % loads
    checks.append(simulate("sky130_core_tt", sky_dir, deck, "dc Vg 0 1.8 0.18",
                           ("Vn", "Vp"), out, args.ngspice_bin))
    ihp_dir = ROOT / ihp["directory"] / "ihp-sg13cmos5l/libs.tech/ngspice/models"
    checks.append(simulate("ihp_cmos5l_pnp_typ", ihp_dir, """IHP exported shared PNP source check
.lib cornerPNP.lib typ
.temp 27
Ve e 0 1.2
Vb b 0 1.2
Vc c 0 0
Xp c b e pnpMPA
.end
""", "dc Vb 1.2 0.5 -0.07", ("Vc",), out, args.ngspice_bin))
    result = {"status": "passed", "recorded_at": datetime.now(timezone.utc).isoformat(),
              "ngspice": subprocess.check_output([args.ngspice_bin, "--version"], text=True).strip(),
              "manifest_sha256": sha((ROOT / "docs/platform-import/manifest.json").read_bytes()),
              "scope": "GF180 typical 3.3/6 V pairs; SKY130 core TT 1.8 V; IHP CMOS5L typ PNP; two rejection controls",
              "checks": checks, "command": "python3 checks/platform_smoke.py --output <unused-external-directory>"}
    (out / "result.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "passed", "checks": len(checks), "result": str(out / "result.json")}))


if __name__ == "__main__":
    main()
