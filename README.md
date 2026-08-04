# QREntropy

A modular Python framework for "quantum random number generation (QRNG)", "entropy estimation", "randomness certification", and "noise analysis", built on Qiskit.

QREntropy simulates several quantum circuits designed to produce randomness (Hadamard superposition, Bell-state entanglement, GHZ multipartite entanglement), then subjects the resulting bitstreams to entropy measures and statistical randomness tests — including under simulated hardware noise (bit-flip, phase-flip, depolarizing channels) — to study how noise degrades randomness quality.

## Why this project

Quantum measurement outcomes are randomness sources with a physical (not just algorithmic) justification. But real quantum hardware is noisy, and noise can bias or correlate outcomes in ways that undermine that randomness guarantee. QREntropy is a sandbox for exploring that tension: generate bits from different quantum circuit designs, inject controlled noise, and measure exactly how much entropy and statistical quality survive.

## Features

**Generators**
- `HadamardQRNG` — single-qubit superposition-based bit generation
- `BellQRNG` — entangled-pair generation, used to test correlation under noise
- `GHZQRNG` — multipartite GHZ-state generation

**Noise models**
- Bit-flip, phase-flip, and depolarizing channels
- Single-parameter noise sweeps and multi-noise-model comparison sweeps

**Entropy estimation**
- Shannon entropy
- Min-entropy

**Statistical randomness testing**
- Frequency (monobit) test
- Chi-square test
- Runs test
- Autocorrelation test
- Automated randomness and Bell-correlation report generation

**Visualization**
- Circuit diagrams (saved as PNG)
- Entropy-vs-noise and correlation-vs-noise plots
- Multi-noise-model comparison plots

**Backend**
- Qiskit Aer simulator wrapper

## Project structure

```
QREntropy/
├── main.py                    # Entry point — runs the full experiment pipeline
├── src/
│   ├── generators/            # QRNG circuit generators (Hadamard, Bell, GHZ)
│   ├── circuits/               # Underlying circuit definitions
│   ├── entropy/                # Shannon and min-entropy estimators
│   ├── noise/                  # Noise channels and noise-sweep utilities
│   ├── statistics/             # NIST-style statistical randomness tests + reports
│   ├── visualization/          # Plotting utilities
│   ├── backend/                # Simulator backend wrapper
│   ├── extractors/              # Randomness extraction (in progress)
│   └── config.py               # Global experiment configuration
├── results/                    # Generated reports and plots
├── dashboard/                  # Streamlit dashboard (in progress)
├── tests/
└── notebooks/
```

## Installation

Requires Python 3.10+.

```bash
git clone https://github.com/anikatabassum06/qrentropy-qrng-framework.git
cd qrentropy-qrng-framework
pip install -r requirements.txt
```

Key dependencies: `qiskit`, `qiskit-aer`, `numpy`, `scipy`, `matplotlib`, `pandas`, `streamlit`, `pytest`.

## Usage

Run the full experiment pipeline (Hadamard experiment → Bell experiment → noise sweep → multi-noise comparison):

```bash
python main.py
```

This will:
1. Generate bitstrings from the Hadamard and Bell-state circuits and save circuit diagrams to `results/`
2. Run statistical randomness and correlation tests, saving text reports to `results/`
3. Sweep depolarizing noise levels (`0.00` → `0.20`) and plot entropy/correlation degradation
4. Compare multiple noise models side by side

Experiment parameters (qubit count, shot count, output paths) are set in `src/config.py`.

## Sample results

From a 1000-shot Hadamard run (8 qubits, 8000 bits total):

| Metric | Value |
|---|---|
| P(0) / P(1) | 0.4998 / 0.5003 |
| Shannon entropy | 1.000000 bits |
| Balance test | PASS |

From a 1000-shot Bell-state run:

| Metric | Value |
|---|---|
| Correlation rate | 1.000000 |
| Bell pair test | PASS |

Noise-sweep plots (entropy and correlation vs. noise level, single- and multi-model) are saved to `results/` as PNGs.
