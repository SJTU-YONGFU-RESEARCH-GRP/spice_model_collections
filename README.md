# SPICE Model Collections

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![SPICE](https://img.shields.io/badge/SPICE-Models-blue.svg)](https://en.wikipedia.org/wiki/SPICE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_collections/blob/main/CONTRIBUTING.md)

A comprehensive collection of open-source and simplified BSIM (Berkeley Short-channel IGFET Model) SPICE models for circuit simulation, benchmarking, and evaluation. This repository provides ready-to-use transistor models across multiple SPICE simulators including NGSPICE, HSPICE, and SPECTRE.

## 📋 Table of Contents

- [📁 Repository Structure](#-repository-structure)
- [🚀 Quick Start](#-quick-start)
- [📚 Available Models](#-available-models)
- [⚖️ License](#️-license)
- [📞 Support](#-support)
- [🙏 Acknowledgments](#-acknowledgments)

## 📁 Repository Structure

```
spice_model_collections/
├── bsim/                          # BSIM model files
│   ├── nmos_bsim1.hspice         # BSIM1 models for HSPICE
│   ├── nmos_bsim1.ngspice        # BSIM1 models for NGSPICE
│   ├── nmos_bsim1.spectre        # BSIM1 models for SPECTRE
│   ├── nmos_bsim2.hspice         # BSIM2 models
│   └── ...                       # Additional BSIM levels
├── ptm/                           # Predictive Technology Models
│   ├── 180nm_bulk.pm             # 180nm bulk CMOS models
│   ├── 130nm_bulk.pm             # 130nm bulk CMOS models
│   ├── 90nm_bulk.pm              # 90nm bulk CMOS models
│   ├── 65nm_bulk.pm              # 65nm bulk CMOS models
│   └── ...                       # Additional PTM models
│   └── 7pfet_HP.pm               # 7nm PFET high performance
├── MODELS.md                      # Comprehensive parameter reference
└── README.md                      # This file
```

## 🚀 Quick Start

### Prerequisites

- SPICE simulator (NGSPICE, HSPICE, or SPECTRE)
- Basic understanding of SPICE syntax

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_collections.git
   cd spice_model_collections
   ```

2. **Choose your technology and model:**
   - **BSIM Models**: Use files from `bsim/` directory
     - NGSPICE: `.ngspice` files
     - HSPICE: `.hspice` files
     - SPECTRE: `.spectre` files
   - **PTM Models**: Use files from `ptm/` directory (compatible with HSPICE/SPECTRE)

3. **Include models in your SPICE deck:**
   ```spice
   * BSIM4 example
   .include bsim/nmos_bsim4.ngspice

   * PTM 22nm example
   .include ptm/22nm_LP.pm
   ```

## 📚 Available Models

### BSIM Models

| Model | Level | Status | Transistors | Description |
|---|---|---|---|---|
| **Level 1-3** | LEVEL=1-3 | ✅ Available | NMOS & PMOS | Classic SPICE models (Shichman-Hodges, Grove-Frohman, Semi-empirical) |
| **BSIM1** | LEVEL=4 | ✅ Available | NMOS & PMOS | First-generation Berkeley Short-channel IGFET Model |
| **BSIM2** | LEVEL=5 | ✅ Available | NMOS & PMOS | Second-generation BSIM with improved subthreshold and mobility |
| **BSIM3v3** | LEVEL=8 | ✅ Available | NMOS & PMOS | Industry-standard deep submicron threshold voltage and capacitance model |
| **BSIM4** | LEVEL=14 | ✅ Available | NMOS & PMOS | Standard for planar bulk nanometer MOSFETs down to 22nm |
| **BSIM-SOI** | LEVEL=70 | ✅ Available | NMOS & PMOS | Standard compact model for PD-SOI and FD-SOI technologies |
| **BSIM-CMG** | LEVEL=72 | ✅ Available | NMOS & PMOS | Standard compact model for Multi-Gate devices (FinFET, GAAFET, Nanosheet) |
| **BSIM-IMG** | LEVEL=73 | ✅ Available | NMOS & PMOS | Standard compact model for Independent Multi-Gate / UTBB-FDSOI |
| **BSIM-BULK** | LEVEL=77 | ✅ Available | NMOS & PMOS | BSIM6 surface-potential and charge-based standard for bulk CMOS |

### PTM (Predictive Technology Models)

Predictive Technology Models from ASU provide industry-standard transistor models for academic research and benchmarking across multiple technology nodes.

| Technology Node | Transistor Type | Status | Description |
|-----------------|-----------------|--------|-------------|
| **180nm** | Bulk CMOS | ✅ Available | 1.8V supply voltage |
| **130nm** | Bulk CMOS | ✅ Available | 1.5V supply voltage |
| **90nm** | Bulk CMOS | ✅ Available | 1.2V supply voltage |
| **65nm** | Bulk CMOS | ✅ Available | 1.2V supply voltage |
| **45nm** | Low Power (LP) | ✅ Available | 1.1V supply voltage |
| **32nm** | Low Power (LP) | ✅ Available | 1.0V supply voltage |
| **22nm** | Low Power (LP) | ✅ Available | 0.95V supply voltage |
| **22nm** | High Performance (HP) | ✅ Available | 1.0V supply voltage |
| **16nm** | NFET/PFET HP | ✅ Available | 0.7V supply voltage |
| **14nm** | NFET/PFET HP | ✅ Available | 0.8V supply voltage |
| **10nm** | NFET/PFET HP | ✅ Available | 0.75V supply voltage |
| **7nm** | NFET/PFET HP | ✅ Available | 0.7V supply voltage |

**PTM Model Features:**
- BSIM4-based compact models
- Both NMOS and PMOS transistors
- Multiple threshold voltage options (HP/LSTP)
- Validated against ITRS projections
- Widely used in academic research

### Supported Simulators

- **NGSPICE**: Open-source SPICE simulator
- **HSPICE**: Synopsys HSPICE (commercial)
- **SPECTRE**: Cadence SPECTRE (commercial)

## ⚖️ License

This project is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) - see the [LICENSE](LICENSE) file for details.

### Model Licensing Notes

- Models are provided under their respective open source licenses
- Default license for new contributions is CC BY 4.0
- Simplified/educational models may have additional usage restrictions
- Commercial use requires verification of licensing terms
- Please check individual model files for specific licensing information

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_collections/issues)
- **Discussions**: [GitHub Discussions](https://github.com/SJTU-YONGFU-RESEARCH-GRP/spice_model_collections/discussions)
- **Documentation**: [MODELS.md](MODELS.md)

## 🙏 Acknowledgments

- **BSIM Research Group** at UC Berkeley for developing the BSIM models
- **SPICE Community** for maintaining open-source simulation tools
- **Contributors** who help maintain and expand this collection
