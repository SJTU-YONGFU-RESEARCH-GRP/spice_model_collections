
** modelcard
.model nmos_lvt nmos_lvt
+DVTSHIFT=0 u0=0.03 xl=1.2e-8 DeltaWGAA=0 DeltaTGAA=0 EOT_0=1.1e-9

*.model nmos_slvt nmos_slvt
*+DVTSHIFT=-0.065 u0=0.032 xl=1.2e-8 DeltaWGAA=0 DeltaTGAA=0 EOT_0=1.1e-9

*.model nmos_svt nmos_svt
*+DVTSHIFT=0.065 u0=0.027 xl=1.2e-8 DeltaWGAA=0 DeltaTGAA=0 EOT_0=1.1e-9

*.model nmos_sramvt nmos_sramvt
*+DVTSHIFT=0.125 u0=0.027 xl=1.2e-8 DeltaWGAA=0 DeltaTGAA=0 EOT_0=1.1e-9

.model pmos_lvt pmos_lvt
+DVTSHIFT=0 u0=0.03 xl=1.2e-8 DeltaWGAA=0 DeltaTGAA=0 EOT_0=1.1e-9

*.model pmos_slvt pmos_slvt
*+DVTSHIFT=-0.065 u0=0.032 xl=1.2e-8 DeltaWGAA=0 DeltaTGAA=0 EOT_0=1.1e-9

*.model pmos_svt pmos_svt
*+DVTSHIFT=0.065 u0=0.027 xl=1.2e-8 DeltaWGAA=0 DeltaTGAA=0 EOT_0=1.1e-9

*.model pmos_sramvt pmos_sramvt
*+DVTSHIFT=0.125 u0=0.027 xl=1.2e-8 DeltaWGAA=0 DeltaTGAA=0 EOT_0=1.1e-9
