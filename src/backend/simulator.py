from qiskit_aer import AerSimulator


class QuantumSimulator:
    def __init__(self, noise_model=None):
        self.backend = AerSimulator(
            noise_model=noise_model
        )

    def get_backend(self):
        return self.backend