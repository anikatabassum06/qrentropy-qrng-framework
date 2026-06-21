from collections import Counter


class BellCorrelationReport:
    @staticmethod
    def generate(bitstrings: list[str]) -> str:
        total = len(bitstrings)
        counts = Counter(bitstrings)

        count_00 = counts.get("00", 0)
        count_11 = counts.get("11", 0)
        count_01 = counts.get("01", 0)
        count_10 = counts.get("10", 0)

        correlated = count_00 + count_11
        correlation_rate = correlated / total if total else 0

        passed = correlation_rate >= 0.95

        report = f"""
========================================
Bell-State Correlation Report
========================================

Total samples          : {total}

00                     : {count_00}
11                     : {count_11}
01                     : {count_01}
10                     : {count_10}

Correlation Rate       : {correlation_rate:.6f}

Bell Pair Test         : {"PASS" if passed else "FAIL"}
========================================
"""
        return report