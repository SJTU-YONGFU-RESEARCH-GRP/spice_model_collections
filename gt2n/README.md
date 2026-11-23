# GT2N (2nm GAAFET Nanosheet)

## Technology Overview
- **Node:** 2nm Advanced Gate-All-Around Nanosheet FET (GAAFET)
- **Model Standard:** BSIM-CMG (Level 72 / Level 110)
- **Origin:** Georgia Institute of Technology
- **Supported Simulators:** HSPICE, Spectre, Xyce
- **Devices Available:**
  - `nmos` / `pmos`: Multiple nanosheet widths (W=13nm, W=31nm) and multi-Vt flavours:
    - `elvt`: Extreme Low-Vt
    - `ulvt`: Ultra Low-Vt
    - `lvt`: Low-Vt
    - `svt`: Standard-Vt
    - `hvt`: High-Vt
- **Model Library Entries:**
  - `gt2_w13_svt_tt.sp` (Entry: `nfet_typ` / `pfet_typ`)
  - `gt2_w13_lvt_tt.sp`, `gt2_w13_hvt_tt.sp`, etc.
