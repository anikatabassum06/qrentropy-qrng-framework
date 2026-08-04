from qiskit_aer.noise import NoiseModel, pauli_error


class PhaseFlipNoise:
    @staticmethod
    def create(probability: float) -> NoiseModel:
        noise_model = NoiseModel()

        single_qubit_error = pauli_error([
            ("Z", probability),
            ("I", 1 - probability),
        ])

        two_qubit_error = single_qubit_error.tensor(single_qubit_error)

        noise_model.add_all_qubit_quantum_error(single_qubit_error, ["h"])
        noise_model.add_all_qubit_quantum_error(two_qubit_error, ["cx"])

        return noise_model