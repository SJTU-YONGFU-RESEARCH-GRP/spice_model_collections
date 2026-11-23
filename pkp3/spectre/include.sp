**
***********************************************************************
*                 PKU PHIMO-Fusion Model - Verilog-A                 *
***********************************************************************
*
*  Copyright 2025 Peking University, ShenZhen. All rights reserved
*
*  Project Directors : Prof. Lining Zhang, Prof. Ru Huang
*  Authors           : Baokang Peng, Guoyao Cheng, Wu Dai,
*                      Fangxing Zhang, Yu Li, Honglin Wu
*
*  Notes:
*    - GAA global model (Lg: 16-100 nm; WGAA: 10-40 nm).
*    - Current and capacitance merged.
*    - Derived from BSIM-CMG ver.111.2.1 with the fusion modeling
*      technique [B. Peng et al., "PHIMO-NN: Compact Modeling by
*      Fusing Device Physics and Neural Networks for One-Shot
*      Parameterization," IEEE TCAD].
*    - The Verilog-A code corresponds to the model's Python
*      implementation used for training and adopts a re-organized
*      structure for clarity.
*
***********************************************************************


.hdl ./PHIMO/VERILOG-A/PHIMO_NMOS/fusion_ic_nmos_lvt.va
*.hdl ./PHIMO/VERILOG-A/PHIMO_NMOS/fusion_ic_nmos_slvt.va
*.hdl ./PHIMO/VERILOG-A/PHIMO_NMOS/fusion_ic_nmos_svt.va
*.hdl ./PHIMO/VERILOG-A/PHIMO_NMOS/fusion_ic_nmos_sramvt.va
.hdl ./PHIMO/VERILOG-A/PHIMO_PMOS/fusion_ic_pmos_lvt.va
*.hdl ./PHIMO/VERILOG-A/PHIMO_PMOS/fusion_ic_pmos_slvt.va
*.hdl ./PHIMO/VERILOG-A/PHIMO_PMOS/fusion_ic_pmos_svt.va
*.hdl ./PHIMO/VERILOG-A/PHIMO_PMOS/fusion_ic_pmos_sramvt.va

*.include ./PHIMO/MODELCARD/FF_modelcard.pm
*.include ./PHIMO/MODELCARD/FS_modelcard.pm
.include ./PHIMO/MODELCARD/TT_modelcard.pm
*.include ./PHIMO/MODELCARD/SF_modelcard.pm
*.include ./PHIMO/MODELCARD/SS_modelcard.pm
