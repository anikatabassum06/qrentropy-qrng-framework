import os


class ReportWriter:
    @staticmethod
    def save(report: str, filename: str):
        os.makedirs("results", exist_ok=True)

        path = os.path.join("results", filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"✅ Report saved: {path}")