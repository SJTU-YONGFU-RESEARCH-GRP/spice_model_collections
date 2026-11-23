# Snapshot platform_b52e784fe1b9

Do not edit or normalize the model cards. Source provenance, hashes, declared profiles and dependency findings are in [SOURCE.json](SOURCE.json). Runtime outputs belong in an external work directory.

| Model directory | Engine | Native corner | Loads |
| --- | --- | --- | --- |
| `ngspice` | ngspice | `tt` | `include design.ngspice`; `lib sm141064.ngspice section=typical` |
| `ngspice` | ngspice | `ff` | `include design.ngspice`; `lib sm141064.ngspice section=ff` |
| `ngspice` | ngspice | `ss` | `include design.ngspice`; `lib sm141064.ngspice section=ss` |

## Loading example

These load statements are native to the selected profile. Resolve them from model directory `ngspice` below this snapshot (or set the simulator source path to it). Configure the analysis/testbench separately. The copied files themselves do not require the live PDK Platform API.

```spice
.include "design.ngspice"
.lib "sm141064.ngspice" typical
```

Profile options and geometry units must also be applied: `{"geometry": "width_length", "dimension_unit_m": 1.0, "include_base": "file"}`. Do not rename sections to a generic `tt` or assume simulator dialects are interchangeable.

Original per-source/per-file license notices apply. Source notices:

- [cfc7749b96f6_LICENSE](source_notices/cfc7749b96f6_LICENSE)
