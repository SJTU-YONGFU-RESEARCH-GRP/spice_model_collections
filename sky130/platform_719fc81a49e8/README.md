# Snapshot platform_719fc81a49e8

Do not edit or normalize the model cards. Source provenance, hashes, declared profiles and dependency findings are in [SOURCE.json](SOURCE.json). Runtime outputs belong in an external work directory.

| Model directory | Engine | Native corner | Loads |
| --- | --- | --- | --- |
| `.` | ngspice | `tt` | `include models/parameters/lod.spice`; `include cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.corner.spice`; `include cells/pfet_01v8/sky130_fd_pr__pfet_01v8__tt.corner.spice`; `include cells/nfet_01v8/sky130_fd_pr__nfet_01v8__mismatch.corner.spice`; `include cells/pfet_01v8/sky130_fd_pr__pfet_01v8__mismatch.corner.spice` |

## Loading example

These load statements are native to the selected profile. Resolve them from model directory `.` below this snapshot (or set the simulator source path to it). Configure the analysis/testbench separately. The copied files themselves do not require the live PDK Platform API.

```spice
.include "models/parameters/lod.spice"
.include "cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.corner.spice"
.include "cells/pfet_01v8/sky130_fd_pr__pfet_01v8__tt.corner.spice"
.include "cells/nfet_01v8/sky130_fd_pr__nfet_01v8__mismatch.corner.spice"
.include "cells/pfet_01v8/sky130_fd_pr__pfet_01v8__mismatch.corner.spice"
```

Profile options and geometry units must also be applied: `{"options": {"scale": 1e-06}, "geometry": "width_length", "dimension_unit_m": 1e-06, "include_base": "file"}`. Do not rename sections to a generic `tt` or assume simulator dialects are interchangeable.

## Audit findings

These are literal-reference observations, not the result of interpreting every conditional branch. Documentation examples are separate from active include failures.
- `missing_include`: 1

The full-kit entry retains the original invalid include in `cells/nfet_05v0_nvt/sky130_fd_pr__nfet_05v0_nvt.pm3.spice`. Only the explicitly listed 1.8 V core-pair profile was exercised. No model was substituted from another SKY130 release.

Original per-source/per-file license notices apply. Source notices:

- [cfc7749b96f6_LICENSE](source_notices/cfc7749b96f6_LICENSE)
