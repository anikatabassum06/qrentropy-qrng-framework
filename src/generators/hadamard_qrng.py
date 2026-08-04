"""
Hadamard Quantum Random Number Generator.
"""

from qiskit import QuantumCircuit

from src.generators.base_qrng import BaseQRNG


class HadamardQRNG(BaseQRNG):
    def __init__(
        self,
        num_qubits: int = 8,
        shots: int = 1000,
        backend=None,
    ):
        if num_qubits <= 0:
            raise ValueError("num_qubits must be greater than 0.")

        super().__init__(
            shots=shots,
            backend=backend,
        )

        self.num_qubits = num_qubits

    def build_circuit(self) -> QuantumCircuit:
        circuit = QuantumCircuit(
            self.num_qubits,
            self.num_qubits,
        )

        for qubit in range(self.num_qubits):
            circuit.h(qubit)

        circuit.measure(
            range(self.num_qubits),
            range(self.num_qubits),
        )

        return circuit