import os

import matplotlib.pyplot as plt
from qiskit.visualization import circuit_drawer

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


def save_circuit_image(circuit, filename: str):
    os.makedirs(RESULTS_DIR, exist_ok=True)

    fig = circuit_drawer(circuit, output="mpl")

    image_path = os.path.join(RESULTS_DIR, filename)

    fig.savefig(
        image_path,
        dpi=300,
        bbox_inches="tight",
    )

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


def run_bell_experiment():
    print("\n========================================")
    print("Bell-State QRNG Experiment")
    print("========================================")

    bell_qrng = BellQRNG(shots=SHOTS)

    circuit = bell_qrng.build_circuit()

    if SAVE_CIRCUIT:
        save_circuit_image(circuit, "bell_state_circuit.png")

    bitstrings = bell_qrng.generate_bitstrings()
    integers = BellQRNG.bitstrings_to_integers(bitstrings)

    print("\nBell bitstrings (first 20):")
    print(bitstrings[:20])

    print("\nBell integers (first 20):")
    print(integers[:20])

    report = RandomnessReport.generate(bitstrings)

    print("\n")
    print(report)


def main():
    run_hadamard_experiment()
    run_bell_experiment()


if __name__ == "__main__":
    main()