from qiskit_aer import AerSimulator

def ideal_simulator():
    return AerSimulator(method="statevector")

def noisy_simulator(noise_model):
    return AerSimulator(
        method="density_matrix",
        noise_model=noise_model
    )
