# 🧪 Hardware-Aware Benchmarking of Variational Quantum Algorithms on NISQ Devices

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18212697.svg)](https://doi.org/10.5281/zenodo.18212697)

> A reproducible, hardware-aware benchmarking framework to study the impact of realistic quantum noise on Variational Quantum Algorithms (VQAs) across NISQ-era quantum hardware.

---

## 📌 Abstract

Variational Quantum Algorithms (VQAs) are leading candidates for achieving near-term quantum advantage on Noisy Intermediate-Scale Quantum (NISQ) devices. However, their performance is highly sensitive to hardware-specific noise, gate fidelities, and circuit depth.  
This repository presents a **systematic and reproducible benchmarking framework** that evaluates the degradation of **entanglement, energy estimation, and circuit depth** under realistic noise models inspired by **IBM superconducting qubit systems** and **IonQ trapped-ion architectures**.  

All experiments are implemented using **Qiskit and Aer simulators**, enabling hardware-aware yet fully reproducible analysis suitable for academic research and IEEE-style publications.

---

## 🎯 Objectives

- Benchmark entanglement degradation under realistic noise
- Compare IBM-like and IonQ-like hardware behavior
- Analyze VQA energy estimation robustness under noise
- Study depth-normalized entanglement decay
- Demonstrate hardware-aware error mitigation techniques
- Provide a fully reproducible research pipeline

---

## ✨ Key Contributions

- Hardware-aware noise modeling for superconducting (CZ-based) and trapped-ion systems
- Bell-state entanglement benchmarking under increasing noise
- Entanglement metrics: **Concurrence, Fidelity, Negativity**
- Energy vs noise analysis for variational ansätze
- Depth-normalized entanglement decay comparison
- Zero-Noise Extrapolation (ZNE) for error mitigation
- Transpilation-aware circuit depth and gate analysis
- Publication-ready, reproducible experimental workflow

---

## 🧠 Methodology

### 1️⃣ Ideal Baseline
- Bell-state preparation
- Ideal statevector simulation
- Analytical entanglement verification

### 2️⃣ Hardware-Aware Noise Modeling
- Depolarizing and gate-specific noise
- CZ gate noise for IBM-like superconducting hardware
- Two-qubit interaction noise for IonQ-like trapped-ion systems

### 3️⃣ Entanglement Analysis
- Density matrix simulation
- Concurrence, fidelity, and negativity computation
- Noise-dependent entanglement decay curves

### 4️⃣ Variational Energy Estimation
- Parametric variational ansatz
- Expectation value estimation under noise
- Energy degradation analysis vs hardware error

### 5️⃣ Error Mitigation
- Zero-Noise Extrapolation (ZNE)
- Comparison of noisy vs mitigated results

---

## 📊 Results and Figures

All figures are generated programmatically and saved to the `figures/` directory.

| Figure | Description |
|------|------------|
| `entanglement_decay.png` | Concurrence vs noise strength |
| `hardware_comparison.png` | IBM vs IonQ entanglement decay |
| `energy_vs_noise.png` | VQA energy vs hardware noise |
| `depth_analysis.png` | Depth-normalized entanglement loss |
| `zne_comparison.png` | Error-mitigated vs noisy results |



## ⚙️ Installation

### 🔹 Prerequisites
- Python ≥ 3.9
- pip
- Git

### 🔹 Clone Repository
```bash
git clone https://github.com/MrigankJaiswal-hub/vqa-hardware-benchmark.git
cd vqa-hardware-benchmark



### 🚀 Future Work

Execution on real IBM Quantum and IonQ hardware
Extension to QAOA and larger VQE benchmarks
Advanced error mitigation (PEC, CDR)
Pulse-level noise modeling
ML-assisted hardware-aware ansatz optimization




