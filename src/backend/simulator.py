"""
Backend utilities for QuantumRandLab.
This module provides a wrapper around the Qiskit Aer simulator.
"""

from qiskit_aer import AerSimulator


class QuantumSimulator:
    """
    Wrapper class for the default quantum simulator.
    """

    def __init__(self):
        self.backend = AerSimulator()

    def get_backend(self):
      
        return self.backend