# SPICE Model Collections

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![SPICE](https://img.shields.io/badge/SPICE-Models-blue.svg)](https://en.wikipedia.org/wiki/SPICE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/your-username/spice_model_collections/blob/main/CONTRIBUTING.md)

A comprehensive collection of open-source and simplified BSIM (Berkeley Short-channel IGFET Model) SPICE models for circuit simulation, benchmarking, and evaluation. This repository provides ready-to-use transistor models across multiple SPICE simulators including NGSPICE, HSPICE, and SPECTRE.

## 🎯 Purpose

This project serves the semiconductor and circuit design community by providing:

- **Standardized Model Library**: Consistent, well-documented SPICE models for benchmarking and comparison
- **Cross-Simulator Compatibility**: Models validated across NGSPICE, HSPICE, and SPECTRE simulators
- **Educational Resources**: Comprehensive parameter documentation and usage examples
- **Research Enablement**: Simplified models for academic research and algorithm development
- **Industry Benchmarks**: Reference implementations for circuit design validation

## 📁 Repository Structure

```
spice_model_collections/
├── bsim/                          # BSIM model files
│   ├── nmos_bsim1.hspice         # BSIM1 models for HSPICE
│   ├── nmos_bsim1.ngspice        # BSIM1 models for NGSPICE
│   ├── nmos_bsim1.spectre        # BSIM1 models for SPECTRE
│   ├── nmos_bsim2.hspice         # BSIM2 models
│   └── ...                       # Additional BSIM levels
├── MODELS.md                      # Comprehensive parameter reference
├── README.md                      # This file
└── examples/                      # Usage examples (planned)
```

## 🚀 Quick Start

### Prerequisites

- SPICE simulator (NGSPICE, HSPICE, or SPECTRE)
- Basic understanding of SPICE syntax

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/spice_model_collections.git
   cd spice_model_collections
   ```

2. **Choose your simulator and model:**
   - For NGSPICE: Use `.ngspice` files
   - For HSPICE: Use `.hspice` files
   - For SPECTRE: Use `.spectre` files

3. **Include models in your SPICE deck:**
   ```spice
   .include bsim/nmos_bsim4.ngspice
   ```

## 📚 Available Models

### BSIM Models

| Model | Level | Status | Description |
|-------|-------|--------|-------------|
| **BSIM1** | LEVEL=4 | ✅ Available | First-generation BSIM model |
| **BSIM2** | LEVEL=5 | ✅ Available | Improved short-channel effects |
| **BSIM3v3** | LEVEL=8 | ✅ Available | Industry standard for deep submicron |
| **BSIM4** | LEVEL=14 | ✅ Available | Latest BSIM with advanced features |
| **Level 1-3** | LEVEL=1-3 | ✅ Available | Classic SPICE MOSFET models |

### Supported Simulators

- **NGSPICE**: Open-source SPICE simulator
- **HSPICE**: Synopsys HSPICE (commercial)
- **SPECTRE**: Cadence SPECTRE (commercial)

## 📖 Documentation

### Model Parameters

For detailed parameter definitions and cross-simulator compatibility, see [`MODELS.md`](MODELS.md). This comprehensive reference includes:

- Complete parameter tables for each BSIM level
- Simulator-specific syntax differences
- Parameter evolution through model generations
- Usage guidelines and best practices

### Example Usage

```spice
* Basic inverter simulation with BSIM4
.include bsim/nmos_bsim4.ngspice
.include bsim/pmos_bsim4.ngspice  * (when available)

* Circuit definition
Vdd vdd 0 1.8V
Vin in 0 PULSE(0 1.8 0 10p 10p 1n 2n)

* MOSFET instances
M1 out in vdd vdd PMOS W=1u L=45n
M2 out in 0 0 NMOS W=0.5u L=45n

* Analysis
.tran 10p 10n
.measure tpdr trig v(in) val=0.9 rise=1 targ v(out) val=0.9 fall=1
.measure tpdf trig v(in) val=0.9 fall=1 targ v(out) val=0.9 rise=1

.end
```

## 🔬 Use Cases

### Academic Research
- Algorithm validation for circuit optimization
- Machine learning model training on SPICE data
- Educational demonstrations of MOSFET physics

### Industry Applications
- IP block characterization
- Design rule checking
- Performance benchmarking
- Technology node evaluation

### Circuit Design
- Rapid prototyping with standardized models
- Cross-technology comparison
- Design space exploration

## 🤝 Contributing

We welcome contributions from the community! See our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Ways to Contribute

1. **Add New Models**: Implement additional transistor types, passive components, or technology nodes
2. **Expand Simulator Support**: Add models for LTSPICE, PSpice, or other simulators
3. **Improve Documentation**: Enhance parameter descriptions or add usage examples
4. **Validate Models**: Test models against real silicon data
5. **Bug Reports**: Report inaccuracies or simulation issues

### Model Validation Process

All contributed models undergo:
- Syntax validation across supported simulators
- Basic functionality testing
- Parameter consistency checks
- Documentation review

## 📊 Model Validation

### Current Validation Status

| Model | NGSPICE | HSPICE | SPECTRE | Notes |
|-------|---------|--------|---------|-------|
| BSIM1 NMOS | ✅ | ✅ | ✅ | Basic validation complete |
| BSIM2 NMOS | ✅ | ✅ | ✅ | Basic validation complete |
| BSIM3v3 NMOS | ✅ | ✅ | ✅ | Basic validation complete |
| BSIM4 NMOS | ✅ | ✅ | ✅ | Basic validation complete |

### Validation Metrics

- **DC Characteristics**: ID-VGS, ID-VDS curves
- **AC Performance**: ft, fmax measurements
- **Noise Figure**: NF vs frequency
- **Mismatch Parameters**: Avt, Avt_flk

## ⚖️ License

This project is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) - see the [LICENSE](LICENSE) file for details.

### Model Licensing Notes

- Models are provided under their respective open source licenses
- Default license for new contributions is CC BY 4.0
- Simplified/educational models may have additional usage restrictions
- Commercial use requires verification of licensing terms
- Please check individual model files for specific licensing information

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/spice_model_collections/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/spice_model_collections/discussions)
- **Documentation**: [MODELS.md](MODELS.md)

## 🙏 Acknowledgments

- **BSIM Research Group** at UC Berkeley for developing the BSIM models
- **SPICE Community** for maintaining open-source simulation tools
- **Contributors** who help maintain and expand this collection

## 🔄 Future Plans

- [ ] PMOS model implementations
- [ ] Additional technology nodes (FinFET, Gate-All-Around)
- [ ] Passive component models (resistors, capacitors, inductors)
- [ ] Diode and bipolar transistor models
- [ ] Automated validation test suites
- [ ] Web-based model parameter explorer
- [ ] Integration with circuit design automation tools

---

**Note**: This is an ongoing project. Models provided here are simplified representations intended for educational and benchmarking purposes. For production use, consult with foundry-provided PDKs and validated model decks.
