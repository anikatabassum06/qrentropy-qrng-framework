from collections import Counter
from math import log2


class MinEntropy:
    @staticmethod
    def calculate(bitstring: str) -> float:
        if len(bitstring) == 0:
            return 0.0

        counts = Counter(bitstring)
        total = len(bitstring)

        max_probability = max(counts.values()) / total

        return -log2(max_probability)