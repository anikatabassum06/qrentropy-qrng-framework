"""
Bell-state Quantum Random Number Generator.
"""

from qiskit import transpile

from src.backend.simulator import QuantumSimulator
from src.circuits.bell_state import BellStateCircuit


class BellQRNG:
    def __init__(self, shots: int = 1000):
        if shots <= 0:
            raise ValueError("shots must be greater than 0.")

        self.shots = shots
        self.backend = QuantumSimulator().get_backend()

    def build_circuit(self):
        return BellStateCircuit.build()

    def generate_bitstrings(self) -> list[str]:
        circuit = self.build_circuit()
        compiled_circuit = transpile(circuit, self.backend)

        result = self.backend.run(
            compiled_circuit,
            shots=self.shots,
        ).result()

        counts = result.get_counts()

        bitstrings = []
        for bitstring, count in counts.items():
            bitstrings.extend([bitstring] * count)

        return bitstrings

    @staticmethod
    def bitstrings_to_integers(bitstrings: list[str]) -> list[int]:
        return [int(bitstring, 2) for bitstring in bitstrings]