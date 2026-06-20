"""
Bell-state circuit construction.
"""

from qiskit import QuantumCircuit


class BellStateCircuit:
    @staticmethod
    def build() -> QuantumCircuit:
        circuit = QuantumCircuit(2, 2)

        circuit.h(0)
        circuit.cx(0, 1)

        circuit.measure([0, 1], [0, 1])

        return circuit