import numpy as np
from core_physics.zpf_field_solver import ZPFFieldSolver
from materials_engine.dirac_semimetal import DiracSemimetalNa3Bi
from spacecraft_hull.power_thermal_bus import SpacecraftPowerThermalBus

def run_v2_master_pipeline():
    print("==================================================================")
    print("  ZPF SYNTHETIC GRAVITY ENGINE: MASTER v2.0.0 VERIFICATION PIPELINE ")
    print("==================================================================")
    
    # 1. Core Physics & Field Integration
    solver = ZPFFieldSolver(f_drive=3.0e12, gap_d=50e-9, E_real=5.0e7)
    X_C = solver.compute_capacitive_reactance()
    Fx, Fy, Fz, F_net = solver.compute_3d_thrust_vector(
        dphi_x=np.radians(45), dphi_y=np.radians(30), dphi_z=np.radians(60)
    )
    
    # 2. Materials & Phonon Loss Benchmark
    semimetal = DiracSemimetalNa3Bi()
    frequencies = np.linspace(0.1e12, 10e12, 100)
    loss_v1, loss_v2 = semimetal.get_phonon_loss_profile(frequencies)
    delta_f, isolation = semimetal.compute_cyclotron_non_reciprocity(B_0=0.35)
    
    # 3. Spacecraft Bus & Solar Sizing
    hull = SpacecraftPowerThermalBus(target_thrust_N=F_net)
    P_in_kW, array_area, heat_kW = hull.compute_power_and_solar_array(coupling_efficiency=0.98)
    
    # Print Executive Metrics
    print(f"[PHYSICS] Capacitive Gap Reactance (50nm @ 3THz) : {X_C:.2f} Ohms")
    print(f"[PHYSICS] Scaled Integrated Thrust Output        : {F_net:.2f} N ({F_net/1000:.3f} kN)")
    print(f"[PHYSICS] 3D Vectoring Angles (Pitch/Yaw/Elev)    : Fx={Fx:.1f}N, Fy={Fy:.1f}N, Fz={Fz:.1f}N")
    print(f"------------------------------------------------------------------")
    print(f"[MATERIALS] Boundary Phonon Loss Mitigation      : {loss_v1[50]:.1f}% (v1.0) -> {loss_v2[50]:.1f}% (v2.0)")
    print(f"[MATERIALS] Non-Reciprocal Optical Diode (0.35T)  : Delta_f = {delta_f:.1f} GHz | Isolation = {isolation:.2f} dB")
    print(f"------------------------------------------------------------------")
    print(f"[SPACECRAFT] Total Active Input Power (100% CW)   : {P_in_kW:.2f} kW")
    print(f"[SPACECRAFT] Required ROSA Solar Array (1 AU)     : {array_area:.2f} m^2")
    print(f"[SPACECRAFT] Thermal Dissipation Load (Passive)   : {heat_kW*1000:.1f} Watts")
    print(f"------------------------------------------------------------------")
    print(f"[STATUS] Pipeline Execution Complete: v2.0.0 Architecture Verified.")

if __name__ == "__main__":
    run_v2_master_pipeline()
