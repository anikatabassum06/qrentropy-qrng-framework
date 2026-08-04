"""
Experiment runner for QuantumRandLab.
"""

from src.statistics.randomness_report import RandomnessReport
from src.statistics.bell_correlation_report import BellCorrelationReport
from src.utils.report_writer import ReportWriter


class ExperimentRunner:
    @staticmethod
    def run_randomness_experiment(
        generator,
        name: str,
        report_filename: str,
    ):
        print("\n========================================")
        print(f"{name} QRNG Experiment")
        print("========================================")

        bitstrings = generator.generate_bitstrings()
        integers = generator.bitstrings_to_integers(bitstrings)

        print("\nBitstrings (first 20):")
        print(bitstrings[:20])

        print("\nIntegers (first 20):")
        print(integers[:20])

        report = RandomnessReport.generate(bitstrings)

        print("\n")
        print(report)

        ReportWriter.save(report, report_filename)

        return {
            "name": name,
            "bitstrings": bitstrings,
            "integers": integers,
            "report": report,
        }

    @staticmethod
    def run_correlation_experiment(
        generator,
        name: str,
        report_filename: str,
    ):
        print("\n========================================")
        print(f"{name} Correlation Experiment")
        print("========================================")

        bitstrings = generator.generate_bitstrings()
        integers = generator.bitstrings_to_integers(bitstrings)

        print("\nBitstrings (first 20):")
        print(bitstrings[:20])

        print("\nIntegers (first 20):")
        print(integers[:20])

        report = BellCorrelationReport.generate(bitstrings)

        print("\n")
        print(report)

        ReportWriter.save(report, report_filename)

        return {
            "name": name,
            "bitstrings": bitstrings,
            "integers": integers,
            "report": report,
        }