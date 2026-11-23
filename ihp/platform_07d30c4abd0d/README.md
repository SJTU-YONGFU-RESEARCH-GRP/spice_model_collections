# Snapshot platform_07d30c4abd0d

Do not edit or normalize the model cards. Source provenance, hashes, declared profiles and dependency findings are in [SOURCE.json](SOURCE.json). Runtime outputs belong in an external work directory.

| Model directory | Engine | Native corner | Loads |
| --- | --- | --- | --- |
| `ihp-sg13g2/libs.tech/ngspice/models` | ngspice | `tt` | `lib cornerMOSlv.lib section=mos_tt` |
| `ihp-sg13g2/libs.tech/ngspice/models` | ngspice | `ff` | `lib cornerMOSlv.lib section=mos_ff` |
| `ihp-sg13g2/libs.tech/ngspice/models` | ngspice | `ss` | `lib cornerMOSlv.lib section=mos_ss` |

## Loading example

These load statements are native to the selected profile. Resolve them from model directory `ihp-sg13g2/libs.tech/ngspice/models` below this snapshot (or set the simulator source path to it). Configure the analysis/testbench separately. The copied files themselves do not require the live PDK Platform API.

```spice
.lib "cornerMOSlv.lib" mos_tt
```

Profile options and geometry units must also be applied: `{"geometry": "width_length", "dimension_unit_m": 1.0, "include_base": "file"}`. Do not rename sections to a generic `tt` or assume simulator dialects are interchangeable.

## Audit findings

These are literal-reference observations, not the result of interpreting every conditional branch. Documentation examples are separate from active include failures.
- `tool_header`: 15

SG13CMOS5L and SG13G2 share this one directory tree. Their relative includes and Verilog-A sources remain together. The representative PNP check passes without compiling MOS models; MOS/OSDI compilation remains unverified because the current OpenVAF executable cannot load `libLLVM.so.20.1`. Do not source an entire upstream ngspice startup file that assumes a full installed PDK.

Original per-source/per-file license notices apply. Source notices:

- [c71d239df917_LICENSE](source_notices/c71d239df917_LICENSE)
