# Snapshot platform_29aaf5a8b18c

Do not edit or normalize the model cards. Source provenance, hashes, declared profiles and dependency findings are in [SOURCE.json](SOURCE.json). Runtime outputs belong in an external work directory.

| Model directory | Engine | Native corner | Loads |
| --- | --- | --- | --- |
| `.` | hspice | `tt` | `lib fet.mod section=nfet_typ`; `lib fet.mod section=pfet_typ` |

## Loading example

These load statements are native to the selected profile. Resolve them from model directory `.` below this snapshot (or set the simulator source path to it). Configure the analysis/testbench separately. The copied files themselves do not require the live PDK Platform API.

```spice
.lib "fet.mod" nfet_typ
.lib "fet.mod" pfet_typ
```

Profile options and geometry units must also be applied: `{"geometry": "fin", "include_base": "file"}`. Do not rename sections to a generic `tt` or assume simulator dialects are interchangeable.

Original per-source/per-file license notices apply. Source notices:

- [236a2d5221bb_LICENSE](source_notices/236a2d5221bb_LICENSE)
