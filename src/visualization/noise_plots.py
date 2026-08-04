import os
import matplotlib.pyplot as plt


class NoisePlots:
    @staticmethod
    def plot_hadamard_entropy(results: list[dict], filename: str):
        os.makedirs("results", exist_ok=True)

        noise = [r["noise"] for r in results]
        shannon = [r["shannon_entropy"] for r in results]
        min_entropy = [r["min_entropy"] for r in results]

        plt.figure()
        plt.plot(noise, shannon, marker="o", label="Shannon Entropy")
        plt.plot(noise, min_entropy, marker="o", label="Min Entropy")

        plt.xlabel("Depolarizing Noise Probability")
        plt.ylabel("Entropy")
        plt.title("Hadamard QRNG: Entropy vs Noise")
        plt.legend()
        plt.grid(True)

        path = os.path.join("results", filename)
        plt.savefig(path, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"✅ Plot saved: {path}")

    @staticmethod
    def plot_bell_correlation(results: list[dict], filename: str):
        os.makedirs("results", exist_ok=True)

        noise = [r["noise"] for r in results]
        correlation = [r["correlation_rate"] for r in results]

        plt.figure()
        plt.plot(noise, correlation, marker="o")

        plt.xlabel("Depolarizing Noise Probability")
        plt.ylabel("Bell Correlation Rate")
        plt.title("Bell QRNG: Correlation vs Noise")
        plt.grid(True)

        path = os.path.join("results", filename)
        plt.savefig(path, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"✅ Plot saved: {path}")