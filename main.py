"""
main.py

Entry point for QuantumRandLab.
"""

import os
import matplotlib.pyplot as plt
from qiskit.visualization import circuit_drawer
from src.noise.multi_noise_sweep import MultiNoiseSweep
from src.visualization.multi_noise_plots import MultiNoisePlots

from src.config import (
    NUM_QUBITS,
    SHOTS,
    SHOW_CIRCUIT,
    SAVE_CIRCUIT,
    RESULTS_DIR,
    CIRCUIT_IMAGE_NAME,
)

from src.generators.hadamard_qrng import HadamardQRNG
from src.generators.bell_qrng import BellQRNG

from src.statistics.randomness_report import RandomnessReport
from src.statistics.bell_correlation_report import BellCorrelationReport

from src.utils.report_writer import ReportWriter
from src.noise.noise_sweep import NoiseSweep
from src.visualization.noise_plots import NoisePlots


def save_circuit_image(circuit, filename: str):
    os.makedirs(RESULTS_DIR, exist_ok=True)

    fig = circuit_drawer(circuit, output="mpl")
    image_path = os.path.join(RESULTS_DIR, filename)

    fig.savefig(image_path, dpi=300, bbox_inches="tight")

    if SHOW_CIRCUIT:
        plt.show()
    else:
        plt.close(fig)

    print(f"✅ Quantum circuit saved:\n   {image_path}")


def run_hadamard_experiment():
    print("\n========================================")
    print("Hadamard QRNG Experiment")
    print("========================================")

    qrng = HadamardQRNG(
        num_qubits=NUM_QUBITS,
        shots=SHOTS,
    )

    circuit = qrng.build_circuit()

    if SAVE_CIRCUIT:
        save_circuit_image(circuit, CIRCUIT_IMAGE_NAME)

    bitstrings = qrng.generate_bitstrings()
    integers = HadamardQRNG.bitstrings_to_integers(bitstrings)

    print("\nGenerated bitstrings (first 20):")
    print(bitstrings[:20])

    print("\nGenerated integers (first 20):")
    print(integers[:20])

    report = RandomnessReport.generate(bitstrings)

    print("\n")
    print(report)

    ReportWriter.save(
        report,
        "hadamard_randomness_report.txt",
    )


def run_bell_experiment():
    print("\n========================================")
    print("Bell-State QRNG Experiment")
    print("========================================")

    bell = BellQRNG(shots=SHOTS)

    circuit = bell.build_circuit()

    if SAVE_CIRCUIT:
        save_circuit_image(circuit, "bell_state_circuit.png")

    bitstrings = bell.generate_bitstrings()
    integers = BellQRNG.bitstrings_to_integers(bitstrings)

    print("\nBell bitstrings (first 20):")
    print(bitstrings[:20])

    print("\nBell integers (first 20):")
    print(integers[:20])

    report = BellCorrelationReport.generate(bitstrings)

    print("\n")
    print(report)

    ReportWriter.save(
        report,
        "bell_correlation_report.txt",
    )


def run_noise_sweep():
    print("\n========================================")
    print("Depolarizing Noise Sweep")
    print("========================================")

    noise_levels = [0.00, 0.02, 0.05, 0.10, 0.20]

    hadamard_results = NoiseSweep.run_hadamard(
        noise_levels=noise_levels,
        num_qubits=NUM_QUBITS,
        shots=SHOTS,
    )

    print("\nHadamard QRNG under depolarizing noise:")
    for result in hadamard_results:
        print(
            f"Noise={result['noise']:.2f} | "
            f"Shannon={result['shannon_entropy']:.6f} | "
            f"Min={result['min_entropy']:.6f}"
        )

    bell_results = NoiseSweep.run_bell(
        noise_levels=noise_levels,
        shots=SHOTS,
    )

    print("\nBell QRNG under depolarizing noise:")
    for result in bell_results:
        print(
            f"Noise={result['noise']:.2f} | "
            f"Correlation={result['correlation_rate']:.6f} | "
            f"00={result['00']} | 11={result['11']} | "
            f"01={result['01']} | 10={result['10']}"
        )

    NoisePlots.plot_hadamard_entropy(
        hadamard_results,
        "hadamard_entropy_vs_noise.png",
    )

    NoisePlots.plot_bell_correlation(
        bell_results,
        "bell_correlation_vs_noise.png",
    )

def run_multi_noise_comparison():
    print("\n========================================")
    print("Multi-Noise Comparison")
    print("========================================")

    noise_levels = [0.00, 0.02, 0.05, 0.10, 0.20]

    hadamard_results = MultiNoiseSweep.run_hadamard(
        noise_levels=noise_levels,
        num_qubits=NUM_QUBITS,
        shots=SHOTS,
    )

    bell_results = MultiNoiseSweep.run_bell(
        noise_levels=noise_levels,
        shots=SHOTS,
    )

    MultiNoisePlots.plot_hadamard_entropy(
        hadamard_results,
        "multi_noise_hadamard_entropy.png",
    )

    MultiNoisePlots.plot_bell_correlation(
        bell_results,
        "multi_noise_bell_correlation.png",
    )

    print("✅ Multi-noise comparison completed.")

def main():
    run_hadamard_experiment()
    run_bell_experiment()
    run_noise_sweep()
    run_multi_noise_comparison()

if __name__ == "__main__":
    main()