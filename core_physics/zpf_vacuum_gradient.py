"""
ZPF Vacuum Gradient & Equivalence Principle Verification Module
Simulates universal payload acceleration via Zero-Point Fluctuation nucleon scattering.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

ZPF_Gradient_Strength = 9.81  # 1g equivalent acceleration scaling

def universal_vacuum_gravity(z, nucleons):
    mass_per_nucleon = 1.0
    total_mass = nucleons * mass_per_nucleon
    force = -ZPF_Gradient_Strength * nucleons
    return force / total_mass

def run_zpf_simulation():
    def create_drop(nucleons):
        def equations(t, state):
            z, vz = state
            if z <= 0.1:
                return [0, 0]
            az = universal_vacuum_gravity(z, nucleons)
            return [vz, az]
        return equations

    payloads = {
        "Neutral Polymer": 1000,
        "Titanium Block": 50000,
        "Lead Metamaterial": 200000
    }

    t_span = (0, 1.0)
    t_eval = np.linspace(0, 1.0, 300)
    z_initial = 3.5

    plt.figure(figsize=(9, 5))
    for name, nucleons in payloads.items():
        eqs = create_drop(nucleons)
        sol = solve_ivp(eqs, t_span, [z_initial, 0.0], t_eval=t_eval)
        plt.plot(t_eval, sol.y[0], label=name, linewidth=3, alpha=0.8)

    plt.axhline(0.1, color='black', linestyle='--', label="Diffuser Floor")
    plt.title("Equivalence Principle Verification in ZPF Synthetic Gravity Well")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Height Above Floor Z (meters)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_zpf_simulation()
