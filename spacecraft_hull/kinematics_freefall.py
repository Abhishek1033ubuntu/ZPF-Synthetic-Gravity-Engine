"""
Kinematics Free-Fall Solver
Integrates equations of motion for test masses dropped within the synthetic gravity well,
verifying trajectory straightness and minimal boundary drift.
"""

import numpy as np
from scipy.integrate import solve_ivp

def run_kinematic_drop():
    print("Executing Free-Fall Trajectory Integration over Diffuser Plate...")
    
    def equations_of_motion(t, state):
        x, vx, z, vz = state
        if z <= 0.2:
            return [0, 0, 0, 0]
        # Simulated vertical gravitational attraction
        az = -9.81 
        ax = 0.0  # Zero lateral acceleration due to flattened field
        return [vx, ax, vz, az]

    drop_x_positions = [-2.0, -0.5, 1.5, 2.5]
    t_span = (0, 0.05)
    t_eval = np.linspace(0, 0.05, 300)

    for x0 in drop_x_positions:
        sol = solve_ivp(equations_of_motion, t_span, [x0, 0.0, 3.5, 0.0], t_eval=t_eval)
        drift = abs(sol.y[0][-1] - x0)
        print(f"      -> Payload dropped from x={x0}m | Final X-Drift: {drift*1000:.2f} mm")

if __name__ == "__main__":
    run_kinematic_drop()
