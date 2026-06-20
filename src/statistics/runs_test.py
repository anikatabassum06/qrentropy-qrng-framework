class RunsTest:
    @staticmethod
    def run(bitstring: str) -> dict:
        if len(bitstring) < 2:
            return {"runs": 0, "passed": False}

        runs = 1
        for i in range(1, len(bitstring)):
            if bitstring[i] != bitstring[i - 1]:
                runs += 1

        expected_runs = (len(bitstring) + 1) / 2
        tolerance = 0.10 * expected_runs

        passed = abs(runs - expected_runs) <= tolerance

        return {
            "runs": runs,
            "expected_runs": expected_runs,
            "passed": passed,
        }