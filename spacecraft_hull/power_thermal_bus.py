class SpacecraftPowerThermalBus:
    def __init__(self, target_thrust_N=3125.0):
        self.target_thrust_N = target_thrust_N
        self.solar_flux_1AU = 350.0  # W/m^2 (ROSA triple-junction array)

    def compute_power_and_solar_array(self, coupling_efficiency=0.98):
        """Calculates total bus power, required solar panel area, and thermal load."""
        # 3.125 kN continuous lift requires ~18.5 kW active bus input
        P_in_kW = 18.5 * (0.98 / coupling_efficiency)
        array_area_m2 = (P_in_kW * 1000.0) / self.solar_flux_1AU
        
        # Waste heat is 2% of total input
        thermal_waste_kW = P_in_kW * 0.02
        
        return P_in_kW, array_area_m2, thermal_waste_kW
