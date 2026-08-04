import os
import matplotlib.pyplot as plt


class MultiNoisePlots:
    @staticmethod
    def plot_hadamard_entropy(all_results: dict, filename: str):
        os.makedirs("results", exist_ok=True)

        plt.figure()

        for noise_name, results in all_results.items():
            noise = [r["noise"] for r in results]
            shannon = [r["shannon_entropy"] for r in results]

            plt.plot(noise, shannon, marker="o", label=noise_name)

        plt.xlabel("Noise Probability")
        plt.ylabel("Shannon Entropy")
        plt.title("Hadamard QRNG: Entropy Comparison Across Noise Models")
        plt.legend()
        plt.grid(True)

        path = os.path.join("results", filename)
        plt.savefig(path, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"✅ Plot saved: {path}")

    @staticmethod
    def plot_bell_correlation(all_results: dict, filename: str):
        os.makedirs("results", exist_ok=True)

        plt.figure()

        for noise_name, results in all_results.items():
            noise = [r["noise"] for r in results]
            correlation = [r["correlation_rate"] for r in results]

            plt.plot(noise, correlation, marker="o", label=noise_name)

        plt.xlabel("Noise Probability")
        plt.ylabel("Bell Correlation Rate")
        plt.title("Bell QRNG: Correlation Comparison Across Noise Models")
        plt.legend()
        plt.grid(True)

        path = os.path.join("results", filename)
        plt.savefig(path, dpi=300, bbox_inches="tight")
        plt.close()

        print(f"✅ Plot saved: {path}")