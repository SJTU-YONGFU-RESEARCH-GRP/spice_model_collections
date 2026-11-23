# SPICE Model Collections

Publicly redistributable source-pinned model snapshots, alongside the existing `bsim/` and `ptm/` reference models. Native HSPICE/ngspice/Spectre syntax, includes, section names and geometry scales are retained; file availability is not universal simulator compatibility.

## Platform source import — 2026-11-23

**1,356 original source files**, **5 snapshots**, **52.28 MiB**, covering 6 process identities. Model source bytes are unmodified and independently hash-verifiable. [Manifest](docs/platform-import/manifest.json) · [Import notes](docs/platform-import/README.md) · [Validation](docs/platform-import/validation.json)

| Collection | Source license | Validation boundary |
| --- | --- | --- |
| [asap7](asap7/README.md) | Academic / Apache-2.0 | Level 72 BSIM-CMG (TT, FF, SS) |
| [freepdk45](freepdk45/README.md) | Apache-2.0 | Level 54 BSIM4.0 (TT, FF, SS, VTH, VTL) |
| [freepdk15](freepdk15/README.md) | BSD-style; see LICENSE | Source/hashes checked; not run |
| [freepdk3](freepdk3/README.md) | BSD-style; see LICENSE | Source/hashes checked; not run |
| [gf180mcu](gf180mcu/README.md) | Apache-2.0 | Typical 3.3/6 V MOS pairs tested |
| [gt2n](gt2n/README.md) | Academic Research | Georgia Tech 2nm GAAFET Nanosheet BSIM-CMG |
| [gt3](gt3/README.md) | Academic Research | Georgia Tech 3nm GAAFET BSIM-CMG |
| [ihp](ihp/README.md) | Apache-2.0 | BiCMOS PSP103 OpenVAF OSDI + PNP |
| [pkp3](pkp3/README.md) | Academic Research | Peking University 3nm PHIMO-Fusion GAAFET Verilog-A |
| [sky130](sky130/README.md) | Apache-2.0 | Original whole-kit include defect; core pair tested |
| [ICS55](ics55/README.md) | Upstream Apache-2.0 release | Availability record only; no transistor SPICE models |

## Using a snapshot

1. Select a collection and version. Read its README and `SOURCE.json` for native loads, working/model directory, sections, scale, tool headers and missing dependencies.
2. Load those original files in your own external run directory. Use the real corner name (`typical`, `mos_tt`, `TT`, etc.) shown by the profile. Keep the selected snapshot and hashes in your experiment record.
3. Do not substitute complete-kit entries for the tested subset: the imported SKY130 core pair works, while its upstream full-kit entry still has a missing include. IHP PNP checks do not qualify its MOS/OSDI flow.

```sh
# No source checkout or live platform service is needed for offline verification.
python3 scripts/import_platform_models.py verify
python3 -m unittest discover -s scripts -p test_import_platform_models.py
python3 checks/platform_smoke.py --output /tmp/spice-model-smoke-unique
```

The smoke output directory must not already exist. The checks use `ngspice -n`, inspect finite responding DC data, and verify that missing models/sections are rejected even if ngspice exits zero. Other simulators and devices remain untested in this delivery.

## Reproducing the import

Create a local mapping from the manifest's source keys to the matching original checkouts; see [the example](docs/platform-import/source-map.example.json). Machine-local paths stay in that external file.

```sh
python3 scripts/import_platform_models.py plan --source-map /absolute/path/source-map.json
python3 scripts/import_platform_models.py apply --source-map /absolute/path/source-map.json
python3 scripts/import_platform_models.py verify --check-source --source-map /absolute/path/source-map.json
```

The importer refuses differing destinations, source hash changes, boundary escapes and unreviewed public distributions. Repeating an identical import adds no files. It does not download a PDK, run vendor installers or edit model cards.

## License and retained references

Each imported source and third-party file retains its own license; source notices are included in every snapshot. A collection-level documentation license does not relicense vendor model cards, Verilog-A implementations or the retained reference models. Existing `bsim/`, `ptm/` and [MODELS.md](MODELS.md) are preserved. Commercial and redistribution-restricted sources are handled separately in the private team repository; they are not included here. No standalone DRC/LVS, PEX, complete cell/IP library or bulk measurement dataset was imported.
