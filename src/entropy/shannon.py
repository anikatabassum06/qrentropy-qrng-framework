"""
Shannon entropy computation for binary sequences.
"""

from collections import Counter
from math import log2


class ShannonEntropy:
 
    @staticmethod
    def calculate(bitstring: str) -> float:
        """
        Compute Shannon entropy.

        Parameters
        ----------
        bitstring : str
            Binary string consisting of 0s and 1s.

        Returns
        -------
        float
            Shannon entropy in bits.
        """
        if len(bitstring) == 0:
            return 0.0

        counts = Counter(bitstring)
        total = len(bitstring)

        entropy = 0.0

        for count in counts.values():
            probability = count / total
            entropy -= probability * log2(probability)

        return entropy