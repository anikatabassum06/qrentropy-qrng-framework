"""
Bell-State Quantum Random Number Generator.
"""

from src.circuits.bell_state import BellStateCircuit
from src.generators.base_qrng import BaseQRNG


class BellQRNG(BaseQRNG):
    def __init__(
        self,
        shots: int = 1000,
        backend=None,
    ):
        super().__init__(
            shots=shots,
            backend=backend,
        )

    def build_circuit(self):
        return BellStateCircuit.build()