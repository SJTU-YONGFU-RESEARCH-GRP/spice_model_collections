# SPICE Model Collections

Publicly redistributable source-pinned model snapshots, alongside the existing `bsim/` and `ptm/` reference models. Native HSPICE/ngspice/Spectre syntax, includes, section names and geometry scales are retained; file availability is not universal simulator compatibility.

## 1. Platform Source Snapshot Summary

| Collection | Process Node & Architecture | Core Compact Model | Source License | Validation Boundary |
| :--- | :--- | :--- | :--- | :--- |
| [asap7](asap7/README.md) | 7nm Multi-Fin FinFET | BSIM-CMG (Level 72) | Academic / Apache-2.0 | Level 72 BSIM-CMG (TT, FF, SS) |
| [freepdk45](freepdk45/README.md) | 45nm Planar Bulk CMOS | BSIM4.0 (Level 54) | Apache-2.0 | Level 54 BSIM4.0 (TT, FF, SS, VTH, VTL) |
| [freepdk15](freepdk15/README.md) | 15nm Multi-Fin FinFET | BSIM-CMG (Level 72) | BSD-style; see LICENSE | Surface-potential multi-gate FinFET |
| [freepdk3](freepdk3/README.md) | 3nm GAAFET Nanosheet | BSIM-CMG (Level 72) | BSD-style; see LICENSE | Multi-sheet GAAFET electrostatics |
| [gf180mcu](gf180mcu/README.md) | 180nm Bulk CMOS | BSIM4 (Level 54) | Apache-2.0 | Typical 3.3/6.0V Core & IO MOS pairs |
| [gt2n](gt2n/README.md) | 2nm GAAFET Nanosheet | BSIM-CMG (Level 72) | Academic Research | Sub-2nm multi-ribbon GAAFET ($W=13\text{--}26\text{nm}$) |
| [gt3](gt3/README.md) | 3nm GAAFET Nanosheet | BSIM-CMG (Level 72) | Academic Research | Georgia Tech 3nm GAAFET ($L=15\text{nm}$, RVT/LVT) |
| [ihp](ihp/README.md) | 130nm BiCMOS | PSP103.6 (OSDI) + VBIC | Apache-2.0 | OpenVAF compiled OSDI + SiGe HBT |
| [pkp3](pkp3/README.md) | 3nm GAAFET AI/Physics | PHIMO-Fusion (Verilog-A) | Academic Research | Peking University AI/Physics fused GAAFET |
| [sky130](sky130/README.md) | 130nm Bulk CMOS | BSIM4.5 (Level 54) | Apache-2.0 | Subcircuit hierarchical wrapper, 1.8V core pair |
| [ICS55](ics55/README.md) | 55nm Bulk CMOS | Foundry Release | Apache-2.0 | Platform availability record |
| [ptm](ptm/README.md) | 180nm to 7nm Bulk / FinFET | BSIM3v3, BSIM4, BSIM-CMG | ASU Public Research | Predictive scaling technology model cards |
| [bsim](bsim/README.md) | Reference Models | CMC Standard Models | UC Berkeley Open Source | Official reference BSIM3/4/CMG cards |

---

## 2. Device Catalog & Modeling Physics

Each library contains compact models calibrated to specific device physics, geometric dimensions, and manufacturing process corners.

### 2.1 ASAP7 (7nm Predictive FinFET)
- **Architecture**: Sub-10nm multi-fin 3D FinFET geometry ($T_{FIN} = 7\text{ nm}$, $H_{FIN} = 32\text{ nm}$, fin pitch $= 27\text{ nm}$, nominal $L_g = 20\text{ nm}$).
- **Transistor Devices**:
  - `nmos_rvt` / `pmos_rvt`: Regular threshold voltage logic devices ($V_{DD} = 0.70\text{ V}$).
  - `nmos_lvt` / `pmos_lvt`: Low-threshold high-speed logic devices.
  - `nmos_slvt` / `pmos_slvt`: Super-low threshold voltage devices.
  - `nmos_sram` / `pmos_sram`: High-density 6T SRAM bitcell transistors.
- **Model Formulation**: **BSIM-CMG (Berkeley Short-Channel IGFET Model - Compact Multi-Gate, Level 72)**, the industry CMC standard for multi-gate architectures.
- **Physical Modeling**:
  - *Electrostatics*: Surface potential analytically computed from 3-gate wrapping boundary conditions; avoids piecewise fitting artifacts.
  - *Quantum Confinement*: Explicit quantum mechanical subband energy shifts and volume inversion within narrow ($7\text{ nm}$) silicon fins, accurately predicting threshold voltage upward shift ($V_{th}$).
  - *Parasitic Network*: Bias-dependent fin extension resistance ($R_{ext}$), source/drain spreading resistance, and 3D fringing corner capacitance ($C_{fr}$).
  - *Process Corners*: Fast-Fast (`7nm_FF_160803.pm`), Typical-Typical (`7nm_TT_160803.pm`), and Slow-Slow (`7nm_SS_160803.pm`).
- **Simulators**: Synopsys HSPICE, Cadence Spectre, Sandia Xyce.

```spice
* HSPICE / Xyce Usage
.inc asap7/hspice/7nm_TT_160803.pm
M1 drain gate source bulk nmos_rvt L=20n NFIN=2
```

---

### 2.2 FreePDK45 (45nm Planar Bulk CMOS)
- **Architecture**: 45nm planar bulk silicon with high-$\kappa$ metal gate (HKMG) technology ($L_{min} = 45\text{ nm}$, $V_{DD} = 1.0\text{ V}$).
- **Transistor Devices**:
  - `NMOS_VTG` / `PMOS_VTG`: Standard nominal-threshold devices ($V_{th} \approx 0.31\text{ V}$).
  - `NMOS_VTH` / `PMOS_VTH`: High-threshold devices for ultra-low static leakage ($I_{off} < 10\text{ pA}/\mu\text{m}$).
  - `NMOS_VTL` / `PMOS_VTL`: Low-threshold devices for critical timing path overdrive.
  - `NMOS_THKOX` / `PMOS_THKOX`: Thick-oxide 1.8V/2.5V I/O interface transistors.
- **Model Formulation**: **BSIM4.0 (Level 54)**.
- **Physical Modeling**:
  - *Short-Channel Effects*: Accurate modeling of DIBL (drain-induced barrier lowering), $V_{th}$ roll-off, velocity saturation, and channel length modulation (CLM).
  - *Gate Leakage*: Quantum mechanical tunneling through thin gate dielectrics, partitioned into gate-to-channel ($I_{gc}$), gate-to-source ($I_{gs}$), and gate-to-drain ($I_{gd}$) components.
  - *Stress Effects*: Length-of-diffusion (LOD) and layout proximity stress equations.
  - *Process Corners*: Convenience include files (`nom.inc`, `ff.inc`, `ss.inc`) mapping to `tran_models/`.
- **Simulators**: ngspice, Synopsys HSPICE, Cadence Spectre, Sandia Xyce.

```spice
* ngspice / HSPICE Usage
.inc freepdk45/nom.inc
M1 drain gate source bulk NMOS_VTG L=45n W=10u
```

---

### 2.3 FreePDK15 (15nm Multi-Fin FinFET)
- **Architecture**: 15nm FinFET technology node ($L_g = 16\text{ nm}$, fin width $= 8\text{ nm}$, fin height $= 26\text{ nm}$, fin pitch $= 48\text{ nm}$, $V_{DD} = 0.8\text{ V}$).
- **Transistor Devices**:
  - `nfet` / `pfet`: Core symmetric 3-terminal FinFETs with tied gate electrodes.
- **Model Formulation**: **BSIM-CMG Level 72**.
- **Physical Modeling**:
  - *3D Surface Potential*: Multi-gate channel electrostatics capturing the transition from weak to strong inversion without unphysical regional discontinuities.
  - *Short-Channel Control*: Subthreshold swing close to ideal $68\text{ mV/dec}$ due to double-gate electrostatic confinement; minimal drain-induced barrier lowering.
  - *S/D Access Resistance*: Models source/drain contact resistance and fin extension sheet resistance with non-linear bias dependence.
- **Simulators**: Synopsys HSPICE, Cadence Spectre, Sandia Xyce.

```spice
* HSPICE Usage
.lib freepdk15/hspice/fet.inc CMG
M1 drain gate source bulk nfet L=16n NFIN=2
```

---

### 2.4 FreePDK3 (3nm GAAFET Nanosheet)
- **Architecture**: 3nm gate-all-around multi-bridge channel nanosheet FET ($L_g = 15\text{ nm}$, nanosheet thickness $T_{sh} \approx 5\text{ nm}$, sheet width $W_{sh} \approx 20\text{ nm}$, $V_{DD} = 0.7\text{ V}$).
- **Transistor Devices**:
  - `nfet` / `pfet`: Horizontally stacked multi-sheet GAAFET devices.
- **Model Formulation**: **BSIM-CMG Level 72** parameterized for gate-all-around cylindrical/rectangular sheet boundaries.
- **Physical Modeling**:
  - *Omnidirectional Gate Control*: Complete four-side gate wrap suppressing drain field penetration, maintaining high drive current ($I_{on}$) per footprint.
  - *Volume Inversion*: Channel inversion occurring simultaneously throughout the entire nanosheet body, enhancing carrier mobility and transconductance ($G_m$).
  - *Ballistic Injection*: Incorporates high-field velocity overshoot and quasi-ballistic transport parameters for sub-20nm channel lengths.
- **Simulators**: Synopsys HSPICE, Cadence Spectre, Sandia Xyce.

```spice
* HSPICE Usage
.lib freepdk3/hspice/fet.mod nfet_typ
M1 drain gate source bulk nfet L=15n NFIN=2
```

---

### 2.5 GF180MCU (180nm Planar Bulk CMOS)
- **Architecture**: 0.18 $\mu$m commercial 3.3V/6.0V MCU foundry process from GlobalFoundries.
- **Transistor Devices**:
  - `nmos_3p3` / `pmos_3p3`: Standard 3.3V core logic transistors ($L_{min} = 0.28\text{ }\mu\text{m}$).
  - `nmos_6p0` / `pmos_6p0`: 6.0V high-voltage transistors for analog power management and I/O ($L_{min} = 0.70\text{ }\mu\text{m}$).
- **Model Formulation**: **BSIM4 (Level 54)** with comprehensive multi-geometry binning.
- **Physical Modeling**:
  - *Temperature Characterization*: Fully extracted temperature coefficients operating across automotive temperature grade ($-40^\circ\text{C}$ to $+150^\circ\text{C}$).
  - *Statistical Mismatch*: Pelgrom mismatch parameters ($A_{Vth}$, $A_\beta$) and Monte Carlo corner distributions for analog yield analysis.
  - *Substrate Network*: Diode junction leakage (JUNCAP model) and substrate minority carrier injection.
- **Simulators**: ngspice, Sandia Xyce, Synopsys HSPICE, Cadence Spectre.

```spice
* ngspice Usage
.include gf180mcu/ngspice/design.ngspice
.lib models/public-models/gf180mcu/ngspice/sm141064.ngspice typical
M1 drain gate source bulk nmos_3p3 L=0.28u W=10u
```

---

### 2.6 GT3 (3nm Georgia Tech GAAFET)
- **Architecture**: 3nm Nanosheet GAAFET developed by the Georgia Institute of Technology for advanced EDA research ($L_g = 15\text{ nm}$, $V_{DD} = 0.70\text{ V}$).
- **Transistor Devices**:
  - `nmos_rvt` / `pmos_rvt`: Regular threshold voltage nanosheet devices.
  - `nmos_lvt` / `pmos_lvt`: Low threshold voltage devices.
- **Model Formulation**: **BSIM-CMG Level 72**.
- **Physical Modeling**:
  - *Nanosheet Geometry*: Explicitly models sheet width ($W_{sh}$), sheet thickness ($T_{sh}$), vertical nanosheet separation ($T_{sus}$), and effective channel width $W_{eff} = 2 \times N_{sheet} \times (W_{sh} + T_{sh})$.
  - *Electrostatic Quality*: Verified for Gummel symmetry (error $< 10^{-12}$) and zero-bias thermodynamic passivity (leakage $< 10^{-15}\text{ A}$).
  - *Self-Heating Effect*: Optional thermal resistance ($R_{th}$) and thermal capacitance ($C_{th}$) network modeling localized temperature rise during switching.
- **Simulators**: Synopsys HSPICE, Cadence Spectre, Sandia Xyce.

```spice
* HSPICE Usage
.inc gt3/hspice/gt3_rvt.mod
M1 drain gate source bulk nmos_rvt L=15n W=10u NFIN=2
```

---

### 2.7 GT2N (2nm Georgia Tech Advanced GAAFET Nanosheet)
- **Architecture**: Sub-2nm nanosheet technology exploring multi-width ribbon channels ($L_g = 14\text{ nm}$, $V_{DD} = 0.70\text{ V}$).
- **Transistor Devices**:
  - `nmos` / `pmos` across discrete nanosheet ribbon widths: $W = 13\text{ nm}$, $18\text{ nm}$, $22\text{ nm}$, and $26\text{ nm}$.
  - Multi-threshold support: standard-Vt (`svt`), low-Vt (`lvt`), high-Vt (`hvt`).
- **Model Formulation**: **BSIM-CMG Level 72**.
- **Physical Modeling**:
  - *Narrow-Sheet Confinement*: Models carrier mobility degradation and subband splitting in narrow nanosheet ribbons ($W_{sh} = 13\text{ nm}$).
  - *Source-to-Drain Direct Tunneling*: Direct quantum mechanical tunneling through the ultra-short $14\text{ nm}$ gate barrier, defining the fundamental off-state leakage floor.
  - *Corner Process Libraries*: Detailed corner files (`gt2_w13_svt_tt.sp`, `gt2_w13_svt_ff.sp`, `gt2_w13_svt_ss.sp`).
- **Simulators**: Synopsys HSPICE, Cadence Spectre, Sandia Xyce.

```spice
* HSPICE Usage
.lib gt2n/hspice/gt2_w13_svt_tt.sp nfet_typ
M1 drain gate source bulk nmos L=14n W=10u NFIN=2
```

---

### 2.8 IHP SG13G2 (130nm BiCMOS & PSP103 OpenVAF OSDI)
- **Architecture**: 130nm High-Performance BiCMOS from IHP Microelectronics featuring sub-micron bulk CMOS and high-speed SiGe:C Heterojunction Bipolar Transistors ($f_T / f_{max} = 300 / 350\text{ GHz}$).
- **Transistor Devices**:
  - `sg13_lv_nmos` / `sg13_lv_pmos`: 1.2V core CMOS transistors ($L_{min} = 0.13\text{ }\mu\text{m}$, $T_{ox} = 2.24\text{ nm}$).
  - `sg13_hv_nmos` / `sg13_hv_pmos`: 3.3V high-voltage CMOS transistors ($T_{ox} = 6.8\text{ nm}$).
  - `npn13G2`: High-speed SiGe:C HBT with carbon doping suppressing boron diffusion.
  - `r3_cmc`: High-precision poly-resistor model.
- **Model Formulation**: **PSP 103.6** (Surface-potential-based compact model, CMC standard) compiled with OpenVAF into OSDI dynamic shared libraries (`pspnqs103va`), plus VBIC for bipolar HBTs.
- **Physical Modeling**:
  - *Surface-Potential Core*: Eliminates unphysical threshold voltage inflection points; continuous higher-order derivatives ($\partial^2 I_d / \partial V_g^2$, $\partial^3 I_d / \partial V_g^3$) essential for RF distortion and harmonic intercept ($IP_3$) modeling.
  - *Non-Quasi-Static (NQS) Dynamics*: Channel relaxation delay modeled via internal transmission-line charge redistribution for microwave frequencies.
  - *Gate Tunneling & JUNCAP2*: Bias-dependent gate oxide leakage currents and non-ideal asymmetric junction capacitances.
- **Simulators**: ngspice (via dynamic OSDI loader), Sandia Xyce, Cadence Spectre, Synopsys HSPICE.

```spice
* ngspice OSDI Usage (requires osdi psp103_nqs.osdi in .spiceinit)
.lib ihp/platform_07d30c4abd0d/ihp-sg13g2/libs.tech/ngspice/models/cornerMOSlv.lib mos_tt
X1 drain gate source bulk sg13_lv_nmos w=10u l=0.34u ng=1
```

---

### 2.9 PKP3 (3nm Peking University PHIMO-Fusion GAAFET)
- **Architecture**: 3nm GAAFET compact model developed by Peking University integrating Physics-Informed Neural Operators with physical semiconductor equations.
- **Transistor Devices**:
  - `nmos_lvt`, `nmos_rvt`, `pmos_lvt`, `pmos_rvt` ($L_g = 16\text{ nm}$, $W = 20\text{ nm}$, $V_{DD} = 0.70\text{ V}$).
- **Model Formulation**: **PHIMO-Fusion AI/Physics Fused Model** implemented in Verilog-A (`fusion_ic_nmos_lvt.va`) with Spectre parameter cards (`TT_modelcard.pm`, `FF_modelcard.pm`, `SS_modelcard.pm`).
- **Physical Modeling**:
  - *Physics/AI Hybrid Architecture*: The core analytical engine enforces fundamental thermodynamic laws: zero-bias passivity ($I(0)=0$), Gummel symmetry ($I_d(V_d, V_s) = -I_s(V_s, V_d)$), and asymptotic boundaries.
  - *Neural Operators*: Physics-constrained neural sub-networks capture sub-3nm multi-subband ballistic transport, 2D quantum wave-function penetration into gate dielectrics, and parasitic sheet-to-sheet coupling capacitances.
  - *Numerical Robustness*: Guaranteed $C_\infty$ smoothness without spurious ripples or unphysical negative conductances ($G_{ds} > 0$).
- **Simulators**: Cadence Spectre (native AHDL Verilog-A compiler), Sandia Xyce.

```spice
* Cadence Spectre Netlist
ahdl_include "pkp3/spectre/fusion_ic_nmos_lvt.va"
include "pkp3/spectre/TT_modelcard.pm"
M1 (drain gate source bulk) nmos_lvt
```

---

### 2.10 SkyWater SKY130 (130nm Planar Bulk CMOS)
- **Architecture**: 130nm internal-foundry Bulk CMOS open-source process with 1.8V core, 5.0V I/O, and non-volatile SONOS flash cells.
- **Transistor Devices**:
  - `nfet_01v8` / `pfet_01v8`: Standard 1.8V logic transistors ($L_{min} = 0.15\text{ }\mu\text{m}$, $W_{min} = 0.42\text{ }\mu\text{m}$).
  - `nfet_01v8_lvt` / `pfet_01v8_hvt`: Low-Vt and high-Vt threshold variants.
  - `nfet_g5v0d10v5`: 5.0V/10.5V extended drain high-voltage transistors.
- **Model Formulation**: **BSIM4.5 (Level 54)** inside hierarchical subcircuit macro-models.
- **Physical Modeling**:
  - *Layout-Dependent Effects*: Full models for length of diffusion (LOD), well proximity effect (WPE), shallow trench isolation (STI) stress, and gate poly spacing.
  - *Parasitic Subcircuits*: Core BSIM4 device coupled with external junction diodes, substrate tap resistors, and gate electrode parasitic resistances.
  - *Spectre-to-ngspice Compatibility*: Evaluated via `parameters/invariant.spice` and corner cards.
- **Simulators**: ngspice (Spectre-compatibility mode), Sandia Xyce, Synopsys HSPICE, Cadence Spectre.

```spice
* ngspice Usage
.include sky130/spice/parameters/invariant.spice
.include sky130/cells/nfet_01v8/sky130_fd_pr__nfet_01v8__tt.pm3.spice
X1 drain gate source bulk sky130_fd_pr__nfet_01v8 w=10 l=0.15
```

---

### 2.11 PTM (Predictive Technology Model)
- **Source**: Arizona State University Nanoscale Integration and Modeling (NIMO) Group.
- **Coverage**: Comprehensive roadmap-predictive model cards spanning:
  - *Bulk CMOS*: 180nm, 130nm, 90nm, 65nm, 45nm, 32nm, 22nm, 16nm.
  - *Multi-Gate FinFET (PTM-MG)*: 20nm, 16nm, 14nm, 10nm, 7nm.
  - *High-$\kappa$ / Metal Gate (PTM-HK)*: 45nm, 32nm, 22nm.
- **Model Formulation**: BSIM3v3, BSIM4, and BSIM-CMG.
- **Usage**: Benchmarking physical scaling trends, exploratory architecture evaluation, and educational curriculum without commercial NDA restrictions.

---

### 2.12 BSIM Reference Models
- **Source**: UC Berkeley Device Group (CMC Industry Standard Reference Releases).
- **Coverage**: Reference test suites and baseline model cards for:
  - `BSIM3v3.3`: Standard sub-micron planar bulk CMOS.
  - `BSIM4.8.2`: Nanoscale bulk CMOS with halo doping and stress effects.
  - `BSIM-CMG 111.2.0`: Standard compact multi-gate FinFET & GAAFET model.
  - `BSIM-IMG 103.0.0`: Independent multi-gate ultra-thin body SOI (FD-SOI).
- **Usage**: Serves as the golden reference standard for validating simulator numerical engine accuracy against the CMC reference implementation.

---

## 3. Simulator Compatibility & Command Matrix

| PDK / Model | ngspice | Synopsys HSPICE | Cadence Spectre | Sandia Xyce | Native Directives & Syntax |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **FreePDK45** | ✓ | ✓ | ✓ | ✓ | `.inc freepdk45/nom.inc` |
| **GF180MCU** | ✓ | ✓ | ✓ | ✓ | `.lib gf180mcu/.../cornerMOSlv.lib mos_tt` |
| **SkyWater SKY130** | ✓ | ✓ | ✓ | ✓ | `.include sky130/.../invariant.spice` + `.pm3.spice` |
| **IHP SG13G2** | ✓ (OSDI) | ✓ | ✓ | ✓ | `osdi psp103_nqs.osdi` + `.lib cornerMOSlv.lib mos_tt` |
| **ASAP7** | - | ✓ | ✓ | ✓ | `.inc asap7/hspice/7nm_TT_160803.pm` (`NFIN=2`) |
| **FreePDK15** | - | ✓ | ✓ | ✓ | `.lib freepdk15/hspice/fet.inc CMG` (`NFIN=2`) |
| **FreePDK3** | - | ✓ | ✓ | ✓ | `.lib freepdk3/hspice/fet.mod nfet_typ` (`NFIN=2`) |
| **GT3** | - | ✓ | ✓ | ✓ | `.inc gt3/hspice/gt3_rvt.mod` (`NFIN=2`) |
| **GT2N** | - | ✓ | ✓ | ✓ | `.lib gt2n/hspice/gt2_w13_svt_tt.sp nfet_typ` |
| **PKP3** | - | - | ✓ | ✓ | `ahdl_include "pkp3/.../fusion_ic_nmos_lvt.va"` |

---

## 4. Verification & Quality Gates (IEEE Standards)

All models in this repository are verified against the physical quality criteria established in **McAndrew et al. (IEEE TED 2025)** and **NeuralCM-QA (IEEE TCAD 2026)**:
1. **Zero-Bias Thermodynamic Passivity**: Terminal currents at equilibrium must vanish ($\sum |I_{terminal}| = 0\text{ A}$) to prevent non-physical energy generation.
2. **Gummel Symmetry Test (GST)**: Under anti-symmetric bias ($V_d = +V_x/2$, $V_s = -V_x/2$), drain-source current must exhibit exact odd symmetry ($I_x(-V_x) = -I_x(V_x)$) with odd derivative continuity ($\partial^2 I_x / \partial V_x^2|_{V_x=0} = 0$).
3. **Transconductance Ripple Auditing**: First and second transconductance derivatives ($G_m = \partial I_d / \partial V_g$, $G_{m2} = \partial^2 I_d / \partial V_g^2$) must remain smooth and monotonic in subthreshold, linear, and saturation regions without spurious oscillations.
4. **Asymptotic Limits**: Device currents must saturate cleanly at high bias without unphysical divergence or negative differential resistance.

---

## 5. License & Redistribution

Each imported source and third-party file retains its original license terms. Source notices are included in every snapshot directory. Standard reference models (`bsim/`, `ptm/`) are released under their respective open academic and UC Berkeley open-source licenses. Commercial and NDA-restricted materials are maintained separately and are not distributed in this public collection.
