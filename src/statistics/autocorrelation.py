class AutocorrelationTest:
    @staticmethod
    def run(bitstring: str, lag: int = 1, tolerance: float = 0.05) -> dict:
        n = len(bitstring)

        if n <= lag:
            return {"correlation": 0, "passed": False}

        matches = 0
        for i in range(n - lag):
            if bitstring[i] == bitstring[i + lag]:
                matches += 1

        correlation = matches / (n - lag)

        return {
            "lag": lag,
            "correlation": correlation,
            "passed": abs(correlation - 0.5) <= tolerance,
        }