"""
GHZ-state circuit construction.

A 3-qubit GHZ state is:

(|000> + |111>) / sqrt(2)
"""

from qiskit import QuantumCircuit


class GHZStateCircuit:
    @staticmethod
    def build(num_qubits: int = 3) -> QuantumCircuit:
        if num_qubits < 3:
            raise ValueError("GHZ state requires at least 3 qubits.")

        circuit = QuantumCircuit(num_qubits, num_qubits)

        circuit.h(0)

        for qubit in range(1, num_qubits):
            circuit.cx(0, qubit)

        circuit.measure(
            range(num_qubits),
            range(num_qubits),
        )

        return circuit