from collections import Counter

from src.entropy.shannon import ShannonEntropy
from src.statistics.frequency_test import FrequencyTest
from src.statistics.chi_square import ChiSquareTest
from src.statistics.runs_test import RunsTest
from src.statistics.autocorrelation import AutocorrelationTest
from src.entropy.min_entropy import MinEntropy


class RandomnessReport:
    @staticmethod
    def generate(bitstrings: list[str]) -> str:
        combined_bits = "".join(bitstrings)
        total_bits = len(combined_bits)

        counts = Counter(combined_bits)
        zeros = counts.get("0", 0)
        ones = counts.get("1", 0)

        p_zero = zeros / total_bits if total_bits > 0 else 0
        p_one = ones / total_bits if total_bits > 0 else 0

        entropy = ShannonEntropy.calculate(combined_bits)
        min_entropy = MinEntropy.calculate(combined_bits)

        frequency = FrequencyTest.run(combined_bits)
        chi_square = ChiSquareTest.run(combined_bits)
        runs = RunsTest.run(combined_bits)
        autocorrelation = AutocorrelationTest.run(combined_bits)

        overall_pass = all([
            frequency["passed"],
            chi_square["passed"],
            runs["passed"],
            autocorrelation["passed"],
        ])

        report = f"""
========================================
QuantumRandLab Randomness Report
========================================

Total bitstrings        : {len(bitstrings)}
Total bits              : {total_bits}

Zeros                   : {zeros}
Ones                    : {ones}

P(0)                    : {p_zero:.6f}
P(1)                    : {p_one:.6f}

Shannon Entropy         : {entropy:.6f} bits
Min Entropy             : {min_entropy:.6f} bits

Frequency Test          : {"PASS" if frequency["passed"] else "FAIL"}
Chi-Square Test         : {"PASS" if chi_square["passed"] else "FAIL"}
Chi-Square Statistic    : {chi_square["chi_square"]:.6f}

Runs Test               : {"PASS" if runs["passed"] else "FAIL"}
Observed Runs           : {runs["runs"]}
Expected Runs           : {runs["expected_runs"]:.2f}

Autocorrelation Test    : {"PASS" if autocorrelation["passed"] else "FAIL"}
Lag                     : {autocorrelation["lag"]}
Correlation             : {autocorrelation["correlation"]:.6f}

Overall Verdict         : {"PASS" if overall_pass else "FAIL"}
========================================
"""
        return report