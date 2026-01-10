from qiskit.quantum_info import SparsePauliOp

def zz_hamiltonian(num_qubits):
    terms = []
    for i in range(num_qubits - 1):
        pauli = ["I"] * num_qubits
        pauli[i] = "Z"
        pauli[i + 1] = "Z"
        terms.append(("".join(pauli), 1.0))
    return SparsePauliOp.from_list(terms)
