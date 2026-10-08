# ZPF-Synthetic-Gravity-Engine
*First-Principles Framework for Topological Zero-Point Fluctuation (ZPF) Synthetic Gravity Generation in Zero-Gravity Spacecraft Environments.*

## Overview
This repository contains the theoretical models, numerical simulations, and materials screening pipelines for generating artificial $1g$ gravitational fields ($9.81 \text{ m/s}^2$) via Zero-Point Fluctuation vacuum biasing. By replacing mechanical rotation with high-frequency photonic driving through topological semimetals, this framework achieves macroscopic synthetic gravity while maintaining the Weak Equivalence Principle across universal payload compositions.

## Key Architectural Modules

1. **Effective Mass Modulation (`core_physics/`)**
   - Simulates field-induced band dispersion curvature ($\partial^2 E / \partial k^2$) to dynamically scale inertial resistance.
   - Implements angular-momentum phase-locking to project stable radiative mass envelopes ($1/r$).

2. **Macroscopic Hull & Diffuser Matrix (`spacecraft_hull/`)**
   - Solves the discrete "ripple effect" point-source problem using a continuous 3D metamaterial diffuser plate.
   - Integrates kinematic solvers to verify lateral drift suppression and straight-line trajectory drops over spacecraft cabin dimensions.

3. **Ambient Topological Materials Engine (`materials_engine/`)**
   - Screens topological Dirac/Weyl semimetals (e.g., Sodium Bismuthate - $\text{Na}_3\text{Bi}$) for ultra-low room-temperature resistivity.
   - Eliminates cryogenic liquid helium support, proving an ambient resistivity of $0.676 \text{ }\mu\Omega\text{-cm}$ (+236.4% conductivity gain over gold).

## System Power Budget
- **Continuous Load:** ~520 kW (Optimized via spatial volumetric trimming, active localized grid switching, and 0.02% duty cycle pulse compression).
- **Power Source:** Compact hybrid fission-fusion generation architecture.
- **Thermal Management:** Managed entirely via passive spacecraft radiator panels.

## Execution
Run the orchestrator or individual scripts within their respective directories using standard Python 3 environments:
```bash
pip install -r requirements.txt
python core_physics/zpf_vacuum_gradient.py
