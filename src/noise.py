from qiskit_aer.noise import NoiseModel, depolarizing_error

def ibm_noise_model(p_2q):
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(
        depolarizing_error(p_2q, 2),
        ["cz"]
    )
    return noise_model

def ionq_noise_model(p_2q):
    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(
        depolarizing_error(p_2q / 5, 2),
        ["xx"]
    )
    return noise_model
