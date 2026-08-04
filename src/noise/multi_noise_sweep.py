from src.backend.simulator import QuantumSimulator
from src.entropy.shannon import ShannonEntropy
from src.entropy.min_entropy import MinEntropy
from src.generators.hadamard_qrng import HadamardQRNG
from src.generators.bell_qrng import BellQRNG

from src.noise.depolarizing import DepolarizingNoise
from src.noise.bit_flip import BitFlipNoise
from src.noise.phase_flip import PhaseFlipNoise


class MultiNoiseSweep:
    NOISE_MODELS = {
        "Depolarizing": DepolarizingNoise,
        "Bit Flip": BitFlipNoise,
        "Phase Flip": PhaseFlipNoise,
    }

    @staticmethod
    def run_hadamard(noise_levels: list[float], num_qubits: int, shots: int):
        all_results = {}

        for noise_name, noise_class in MultiNoiseSweep.NOISE_MODELS.items():
            model_results = []

            for probability in noise_levels:
                noise_model = noise_class.create(probability)
                backend = QuantumSimulator(noise_model=noise_model).get_backend()

                qrng = HadamardQRNG(
                    num_qubits=num_qubits,
                    shots=shots,
                    backend=backend,
                )

                bitstrings = qrng.generate_bitstrings()
                combined_bits = "".join(bitstrings)

                model_results.append({
                    "noise": probability,
                    "shannon_entropy": ShannonEntropy.calculate(combined_bits),
                    "min_entropy": MinEntropy.calculate(combined_bits),
                })

            all_results[noise_name] = model_results

        return all_results

    @staticmethod
    def run_bell(noise_levels: list[float], shots: int):
        all_results = {}

        for noise_name, noise_class in MultiNoiseSweep.NOISE_MODELS.items():
            model_results = []

            for probability in noise_levels:
                noise_model = noise_class.create(probability)
                backend = QuantumSimulator(noise_model=noise_model).get_backend()

                qrng = BellQRNG(
                    shots=shots,
                    backend=backend,
                )

                bitstrings = qrng.generate_bitstrings()

                count_00 = bitstrings.count("00")
                count_11 = bitstrings.count("11")
                count_01 = bitstrings.count("01")
                count_10 = bitstrings.count("10")

                correlation_rate = (count_00 + count_11) / len(bitstrings)

                model_results.append({
                    "noise": probability,
                    "00": count_00,
                    "11": count_11,
                    "01": count_01,
                    "10": count_10,
                    "correlation_rate": correlation_rate,
                })

            all_results[noise_name] = model_results

        return all_results