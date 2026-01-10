import numpy as np
from qiskit.quantum_info import state_fidelity, DensityMatrix
from qiskit.quantum_info.entanglement import concurrence

def fidelity(dm, target_state):
    return state_fidelity(dm, target_state)

def entanglement_concurrence(dm):
    if not isinstance(dm, DensityMatrix):
        dm = DensityMatrix(dm)
    return concurrence(dm)

def energy_expectation(statevector, hamiltonian):
    return np.real(statevector.expectation_value(hamiltonian))
