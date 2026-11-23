# Source-pinned electrical model import

The source files in this public repository are limited to reviewed, redistributable GF180MCU, IHP, SKY130, FreePDK15 and FreePDK3 distributions. Native source licenses and third-party implementation notices remain authoritative. Machine paths, commercial process inventories, proprietary models and service credentials are not part of this repository.

## What was copied

The manifest records each original input key/upstream path, destination, size, SHA-256 and executable bit. Each snapshot's `SOURCE.json` also records native registered profiles, include observations and source notices. Original model data is never rewritten. Internally shared IHP model and Verilog-A trees are kept together. Standard simulator headers are tool dependencies, not copied out of a commercial simulator installation.

## Availability is not qualification

- GF180MCU: typical 3.3 V and 6 V NMOS/PMOS DC sweeps are tested.
- SKY130: only the explicit 1.8 V TT core pair is tested. The original full-kit entry still references `sky130_fd_pr__esd_nfet_05v0_nvt.pm3`, absent from that source. No replacement or alternate release is inserted.
- IHP: SG13CMOS5L typ PNP DC sweep tests the preserved shared-source includes. MOS models need compiled PSP/OSDI modules. The currently checked toolchain fails to load `libLLVM.so.20.1`; no MOS or compiler pass is claimed.
- FreePDK15/3: model bytes, native HSPICE profiles and source licenses are recorded. HSPICE execution was not performed.
- ICS55: only an availability record; CDL connectivity is not a transistor model, so it has no manufactured corner or simulation status.

Missing literal includes, dynamic references and tool headers are separate findings. Static scans do not interpret every branch, encrypted model body or compiled vendor implementation. Whole-file hashes cover every imported byte; large/opaque files do not receive a static-closure claim. Read the validation receipt for the exact measured scope.

## Tools and data

`plan`, `apply` and `verify` use the checked-in manifest. `apply` preflights all inputs before copying, never overwrites a differing destination, and is safe to resume after partial completion. Destinations are regular files, not symlinks back to the source. Git attributes disable EOL normalization for vendor bytes; only generated metadata is treated as ordinary text.

Tests write into an unused external directory and disable user ngspice init files. They do not modify a PDK, a live database, another checkout or a simulator installation. This public import needs no Git LFS; the larger private model packages are a separate delivery.
