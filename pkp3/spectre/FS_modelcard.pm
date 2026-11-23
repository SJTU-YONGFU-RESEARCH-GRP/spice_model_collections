
** modelcard
.model nmos_lvt nmos_lvt
+DVTSHIFT=0 u0=0.031 xl=1.12e-8 DeltaWGAA=0.4e-9 DeltaTGAA=0.2e-9 EOT_0=1.05e-9

.model nmos_slvt nmos_slvt
+DVTSHIFT=-0.065 u0=0.033 xl=1.12e-8 DeltaWGAA=0.4e-9 DeltaTGAA=0.2e-9 EOT_0=1.05e-9

.model nmos_svt nmos_svt
+DVTSHIFT=0.065 u0=0.028 xl=1.12e-8 DeltaWGAA=0.4e-9 DeltaTGAA=0.2e-9 EOT_0=1.05e-9

.model nmos_sramvt nmos_sramvt
+DVTSHIFT=0.125 u0=0.028 xl=1.12e-8 DeltaWGAA=0.4e-9 DeltaTGAA=0.2e-9 EOT_0=1.05e-9



.model pmos_lvt pmos_lvt
+DVTSHIFT=0 u0=0.029 xl=1.28e-8 DeltaWGAA=-0.4e-9 DeltaTGAA=-0.2e-9 EOT_0=1.15e-9

.model pmos_slvt pmos_slvt
+DVTSHIFT=-0.065 u0=0.031 xl=1.28e-8 DeltaWGAA=-0.4e-9 DeltaTGAA=-0.2e-9 EOT_0=1.15e-9

.model pmos_svt pmos_svt
+DVTSHIFT=0.065 u0=0.026 xl=1.28e-8 DeltaWGAA=-0.4e-9 DeltaTGAA=-0.2e-9 EOT_0=1.15e-9

.model pmos_sramvt pmos_sramvt
+DVTSHIFT=0.125 u0=0.026 xl=1.28e-8 DeltaWGAA=-0.4e-9 DeltaTGAA=-0.2e-9 EOT_0=1.15e-9
