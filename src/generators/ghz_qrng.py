"""
GHZ-State Quantum Random Number Generator.
"""

from src.circuits.ghz_state import GHZStateCircuit
from src.generators.base_qrng import BaseQRNG


class GHZQRNG(BaseQRNG):
    def __init__(
        self,
        num_qubits: int = 3,
        shots: int = 1000,
        backend=None,
    ):
        if num_qubits < 3:
            raise ValueError(
                "GHZ QRNG requires at least 3 qubits."
            )

        super().__init__(
            shots=shots,
            backend=backend,
        )

        self.num_qubits = num_qubits

    def build_circuit(self):
        return GHZStateCircuit.build(
            self.num_qubits
        )