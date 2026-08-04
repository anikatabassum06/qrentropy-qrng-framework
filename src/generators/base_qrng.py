"""
Base class for all Quantum Random Number Generators.
"""

import random

from qiskit import transpile

from src.backend.simulator import QuantumSimulator


class BaseQRNG:
    """
    Base class providing common functionality for QRNGs.
    """

    def __init__(self, shots: int = 1000, backend=None):
        if shots <= 0:
            raise ValueError("shots must be greater than zero.")

        self.shots = shots

        if backend is None:
            self.backend = QuantumSimulator().get_backend()
        else:
            self.backend = backend

    def build_circuit(self):
        """
        Must be implemented by subclasses.
        """
        raise NotImplementedError

    def generate_bitstrings(self) -> list[str]:
        circuit = self.build_circuit()

        compiled = transpile(
            circuit,
            self.backend,
        )

        result = self.backend.run(
            compiled,
            shots=self.shots,
        ).result()

        counts = result.get_counts()

        bitstrings = []

        for bitstring, count in counts.items():
            bitstrings.extend(
                [bitstring] * count
            )

        random.shuffle(bitstrings)

        return bitstrings

    @staticmethod
    def bitstrings_to_integers(
        bitstrings: list[str],
    ) -> list[int]:
        return [
            int(bits, 2)
            for bits in bitstrings
        ]