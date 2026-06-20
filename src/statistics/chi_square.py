class ChiSquareTest:
    @staticmethod
    def run(bitstring: str, threshold: float = 3.841) -> dict:
        total = len(bitstring)

        if total == 0:
            return {"chi_square": 0, "passed": False}

        zeros = bitstring.count("0")
        ones = bitstring.count("1")
        expected = total / 2

        chi_square = ((zeros - expected) ** 2 / expected) + (
            (ones - expected) ** 2 / expected
        )

        return {
            "chi_square": chi_square,
            "threshold": threshold,
            "passed": chi_square < threshold,
        }