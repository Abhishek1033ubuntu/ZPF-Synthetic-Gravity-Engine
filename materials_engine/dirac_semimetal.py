import numpy as np

class DiracSemimetalNa3Bi:
    def __init__(self, E_F_eV=0.20, v_F=1.0e6):
        self.e = 1.602176634e-19
        self.v_F = v_F
        self.E_F = E_F_eV * self.e

    def get_phonon_loss_profile(self, frequencies):
        """
        v1.0.0 Direct Ohmic Contact: 65% loss to phonons
        v2.0.0 Capacitive Coupling : 2% flat dielectric relaxation
        """
        loss_v1_ohmic = 65.0 * (1.0 - 1.0 / (1.0 + (frequencies / 1.0e12)**2))
        loss_v2_capacitive = 2.0 * np.ones_like(frequencies)
        return loss_v1_ohmic, loss_v2_capacitive

    def compute_cyclotron_non_reciprocity(self, B_0=0.35, f_drive=3.0e12):
        """Calculates asymmetric frequency splitting under magnetic bias B_0."""
        omega_c = (self.e * B_0 * (self.v_F**2)) / self.E_F
        delta_f_GHz = (omega_c / (2.0 * np.pi)) / 1e9
        isolation_dB = 20.0 * np.log10(1.0 + (omega_c / (2.0 * np.pi * f_drive)))
        return delta_f_GHz, isolation_dB
