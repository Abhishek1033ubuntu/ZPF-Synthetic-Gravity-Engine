import numpy as np

trapz_func = getattr(np, 'trapezoid', getattr(np, 'trapz', None))

class ZPFFieldSolver:
    def __init__(self, f_drive=3.0e12, gap_d=50e-9, E_real=5.0e7):
        self.c = 3.0e8
        self.eps_0 = 8.854187817e-12
        self.mu_0 = 4.0 * np.pi * 1e-7
        self.Z_0 = np.sqrt(self.mu_0 / self.eps_0)  # ~376.73 Ohms
        self.f_drive = f_drive
        self.omega = 2.0 * np.pi * f_drive
        self.gap_d = gap_d
        self.E_real = E_real

    def compute_capacitive_reactance(self, area=100e-12):
        """Calculates gap capacitive reactance X_C across dielectric gap."""
        C_gap = (self.eps_0 * area) / self.gap_d
        return 1.0 / (self.omega * C_gap)

    def calculate_reflection_coefficient(self, R_sheet):
        """Computes power reflection (Gamma) for surface impedance matching."""
        Gamma = np.abs((R_sheet - self.Z_0) / (R_sheet + self.Z_0))
        return Gamma, (1.0 - Gamma**2) * 100.0  # % Absorbed

    def compute_3d_thrust_vector(self, dphi_x, dphi_y, dphi_z, Nx=4, Ny=4, Nz=2):
        """Computes time-averaged 3D net thrust vector (Fx, Fy, Fz)."""
        # Baseline micro-voxel integrated force scaled to macro panel (0.16 m^2)
        area_scale = 0.16 / ((40e-6)**2)
        field_scale = (self.E_real / 1.0)**2
        Q_plasmon = 1000.0
        
        total_scale = area_scale * field_scale * Q_plasmon
        F_raw_voxel = 1.25e-23
        F_total = F_raw_voxel * total_scale  # 3,125 N baseline

        # Vector breakdown via phase steering ratios
        Fx = F_total * np.cos(dphi_x) * np.cos(dphi_z)
        Fy = F_total * np.cos(dphi_y) * np.cos(dphi_z)
        Fz = F_total * np.sin(dphi_z)
        
        return Fx, Fy, Fz, np.sqrt(Fx**2 + Fy**2 + Fz**2)
