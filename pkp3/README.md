# PKP3 (3nm Peking University PHIMO-Fusion GAAFET)

## Technology Overview
- **Node:** 3nm Gate-All-Around Nanosheet FET (GAAFET)
- **Model Standard:** PHIMO-Fusion (Physics-Informed Machine Learning & Compact Modeling)
- **Implementation:** Verilog-A behavioral module + Corner model cards
- **Origin:** Peking University (PKU)
- **Supported Simulators:** Cadence Spectre (native AHDL compilation via `ahdl_include`)
- **Devices Available:**
  - `nmos_lvt`, `nmos_slvt`, `nmos_svt`, `nmos_sramvt`
  - `pmos_lvt`, `pmos_slvt`, `pmos_svt`, `pmos_sramvt`
- **Model Directives:**
  - Verilog-A: `ahdl_include "fusion_ic_nmos_lvt.va"`
  - Model Card: `include "TT_modelcard.pm"` (also FF, SS, SF, FS)
