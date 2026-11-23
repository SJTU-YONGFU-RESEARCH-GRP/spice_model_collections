# Snapshot platform_274a47719724

Do not edit or normalize the model cards. Source provenance, hashes, declared profiles and dependency findings are in [SOURCE.json](SOURCE.json). Runtime outputs belong in an external work directory.

| Model directory | Engine | Native corner | Loads |
| --- | --- | --- | --- |
| `hspice` | hspice | `tt` | `include tran_models/models_nom/NMOS_VTG.inc`; `include tran_models/models_nom/PMOS_VTG.inc`; `include tran_models/models_nom/NMOS_VTL.inc`; `include tran_models/models_nom/PMOS_VTL.inc`; `include tran_models/models_nom/NMOS_VTH.inc`; `include tran_models/models_nom/PMOS_VTH.inc`; `include tran_models/models_nom/NMOS_THKOX.inc`; `include tran_models/models_nom/PMOS_THKOX.inc` |
| `hspice` | hspice | `ff` | `include tran_models/models_ff/NMOS_VTG.inc`; `include tran_models/models_ff/PMOS_VTG.inc`; `include tran_models/models_ff/NMOS_VTL.inc`; `include tran_models/models_ff/PMOS_VTL.inc`; `include tran_models/models_ff/NMOS_VTH.inc`; `include tran_models/models_ff/PMOS_VTH.inc`; `include tran_models/models_ff/NMOS_THKOX.inc`; `include tran_models/models_ff/PMOS_THKOX.inc` |
| `hspice` | hspice | `ss` | `include tran_models/models_ss/NMOS_VTG.inc`; `include tran_models/models_ss/PMOS_VTG.inc`; `include tran_models/models_ss/NMOS_VTL.inc`; `include tran_models/models_ss/PMOS_VTL.inc`; `include tran_models/models_ss/NMOS_VTH.inc`; `include tran_models/models_ss/PMOS_VTH.inc`; `include tran_models/models_ss/NMOS_THKOX.inc`; `include tran_models/models_ss/PMOS_THKOX.inc` |

## Loading example

These load statements are native to the selected profile. Resolve them from model directory `hspice` below this snapshot (or set the simulator source path to it). Configure the analysis/testbench separately. The copied files themselves do not require the live PDK Platform API.

```spice
.include "tran_models/models_nom/NMOS_VTG.inc"
.include "tran_models/models_nom/PMOS_VTG.inc"
.include "tran_models/models_nom/NMOS_VTL.inc"
.include "tran_models/models_nom/PMOS_VTL.inc"
.include "tran_models/models_nom/NMOS_VTH.inc"
.include "tran_models/models_nom/PMOS_VTH.inc"
.include "tran_models/models_nom/NMOS_THKOX.inc"
.include "tran_models/models_nom/PMOS_THKOX.inc"
```

Profile options and geometry units must also be applied: `{"geometry": "width_length", "dimension_unit_m": 1.0, "include_base": "file"}`. Do not rename sections to a generic `tt` or assume simulator dialects are interchangeable.

Some files are encrypted, binary or large enough that only a readable prefix was scanned. Every exported byte was hashed; their hidden/dynamic dependencies and tool/architecture compatibility require a real engine run. This is not a static-closure pass.

Original per-source/per-file license notices apply. Source notices:

See the retained vendor headers and the original licensed distribution; no new redistribution permission is assigned.
