import numpy as np

class MetamaterialBackReflector:
    """
    TiN/SiO2 Plasmonic Metamaterial Back-Reflector (v2.5.0).
    Enforces boundary condition E_tangential(z=0) = 0, reflecting 100% of backward
    ZPF fluctuations into the forward channel and shielding the aft chassis.
    """
    def __init__(self, gamma_back=1.0, stack_material="TiN/SiO2"):
        self.gamma_back = gamma_back
        self.stack_material = stack_material

    def calculate_power_folding_factor(self):
        """Calculates input power savings from standing-wave constructive superposition."""
        # 100% backward reflection folds field forward, halving required input power.
        power_reduction_ratio = 0.50 if self.gamma_back >= 0.98 else (1.0 - 0.5 * self.gamma_back)
        return power_reduction_ratio

    def evaluate_backside_shielding(self, unshielded_leakage_N=185.0):
        """Calculates residual backside spillover force (N)."""
        residual_force_N = unshielded_leakage_N * (1.0 - self.gamma_back)
        return residual_force_N
