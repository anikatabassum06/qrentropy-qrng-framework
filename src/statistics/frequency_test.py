class FrequencyTest:
    @staticmethod
    def run(bitstring: str, tolerance: float = 0.05) -> dict:
        total = len(bitstring)
        zeros = bitstring.count("0")
        ones = bitstring.count("1")

        p_zero = zeros / total if total else 0
        p_one = ones / total if total else 0

        passed = abs(p_zero - p_one) <= tolerance

        return {
            "zeros": zeros,
            "ones": ones,
            "p_zero": p_zero,
            "p_one": p_one,
            "passed": passed,
        }