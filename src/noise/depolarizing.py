from qiskit_aer.noise import NoiseModel, depolarizing_error


class DepolarizingNoise:
    @staticmethod
    def create(probability: float) -> NoiseModel:
        noise_model = NoiseModel()

        single_qubit_error = depolarizing_error(probability, 1)
        two_qubit_error = depolarizing_error(probability, 2)

        noise_model.add_all_qubit_quantum_error(single_qubit_error, ["h"])
        noise_model.add_all_qubit_quantum_error(two_qubit_error, ["cx"])

        return noise_model