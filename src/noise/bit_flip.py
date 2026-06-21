from qiskit_aer.noise import NoiseModel, pauli_error


class BitFlipNoise:
    @staticmethod
    def create(probability: float) -> NoiseModel:
        noise_model = NoiseModel()

        error = pauli_error([
            ("X", probability),
            ("I", 1 - probability),
        ])

        noise_model.add_all_qubit_quantum_error(error, ["h", "cx"])

        return noise_model