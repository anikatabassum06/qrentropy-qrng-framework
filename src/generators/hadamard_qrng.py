"""
Hadamard Quantum Random Number Generator.
"""

from qiskit import QuantumCircuit, transpile

from src.backend.simulator import QuantumSimulator


class HadamardQRNG:
    def __init__(
        self,
        num_qubits: int = 8,
        shots: int = 1000,
        backend=None,
    ):
        if num_qubits <= 0:
            raise ValueError("num_qubits must be greater than 0.")

        if shots <= 0:
            raise ValueError("shots must be greater than 0.")

        self.num_qubits = num_qubits
        self.shots = shots

        if backend is None:
            self.backend = QuantumSimulator().get_backend()
        else:
            self.backend = backend

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

    def generate_bitstrings(self) -> list[str]:
        circuit = self.build_circuit()

        compiled_circuit = transpile(
            circuit,
            self.backend,
        )

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
    def bitstrings_to_integers(
        bitstrings: list[str],
    ) -> list[int]:
        return [
            int(bitstring, 2)
            for bitstring in bitstrings
        ]