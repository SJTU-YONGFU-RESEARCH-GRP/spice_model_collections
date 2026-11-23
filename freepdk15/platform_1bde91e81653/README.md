# Snapshot platform_1bde91e81653

Do not edit or normalize the model cards. Source provenance, hashes, declared profiles and dependency findings are in [SOURCE.json](SOURCE.json). Runtime outputs belong in an external work directory.

| Model directory | Engine | Native corner | Loads |
| --- | --- | --- | --- |
| `.` | hspice | `tt` | `lib fet.inc section=CMG` |

## Loading example

These load statements are native to the selected profile. Resolve them from model directory `.` below this snapshot (or set the simulator source path to it). Configure the analysis/testbench separately. The copied files themselves do not require the live PDK Platform API.

```spice
.lib "fet.inc" CMG
```

Profile options and geometry units must also be applied: `{"geometry": "fin", "include_base": "file"}`. Do not rename sections to a generic `tt` or assume simulator dialects are interchangeable.

Original per-source/per-file license notices apply. Source notices:

- [f4df004102f1_LICENSE](source_notices/f4df004102f1_LICENSE)
