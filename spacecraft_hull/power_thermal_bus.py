class SpacecraftPowerThermalBus:
    def __init__(self, target_thrust_N=3125.0):
        self.target_thrust_N = target_thrust_N
        self.solar_flux_1AU = 350.0  # W/m^2 (ROSA triple-junction array)

    def compute_power_and_solar_array_v25(self, coupling_efficiency=0.98, has_reflector=True):
        """Calculates active bus power, solar panel area, and thermal load for v2.5.0."""
        reflector_multiplier = 0.50 if has_reflector else 1.0
        P_in_kW = 18.5 * (0.98 / coupling_efficiency) * reflector_multiplier  # 9.25 kW
        array_area_m2 = (P_in_kW * 1000.0) / self.solar_flux_1AU                # 26.43 m^2
        thermal_waste_kW = P_in_kW * 0.02                                       # 185 Watts
        
        return P_in_kW, array_area_m2, thermal_waste_kW
        
        # Waste heat is 2% of total input
        thermal_waste_kW = P_in_kW * 0.02
        
        return P_in_kW, array_area_m2, thermal_waste_kW
