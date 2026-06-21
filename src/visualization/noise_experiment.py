from src.noise.depolarizing import DepolarizingNoise


class NoiseExperiment:
    @staticmethod
    def create_depolarizing(probability: float):
        return DepolarizingNoise.create(probability)