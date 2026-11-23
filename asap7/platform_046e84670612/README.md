# Snapshot platform_046e84670612

Do not edit or normalize the model cards. Source provenance, hashes, declared profiles and dependency findings are in [SOURCE.json](SOURCE.json). Runtime outputs belong in an external work directory.

| Model directory | Engine | Native corner | Loads |
| --- | --- | --- | --- |
| `hspice` | hspice | `tt` | `include 7nm_TT_160803.pm` |
| `hspice` | hspice | `ss` | `include 7nm_SS_160803.pm` |
| `hspice` | hspice | `ff` | `include 7nm_FF_160803.pm` |

## Loading example

These load statements are native to the selected profile. Resolve them from model directory `hspice` below this snapshot (or set the simulator source path to it). Configure the analysis/testbench separately. The copied files themselves do not require the live PDK Platform API.

```spice
.include "7nm_TT_160803.pm"
```

Profile options and geometry units must also be applied: `{"geometry": "fin", "include_base": "file"}`. Do not rename sections to a generic `tt` or assume simulator dialects are interchangeable.

Original per-source/per-file license notices apply. Source notices:

- [873eff414f79_COPYRIGHT](source_notices/873eff414f79_COPYRIGHT)
