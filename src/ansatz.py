from qiskit import QuantumCircuit
from qiskit.circuit import Parameter

def hardware_efficient_ansatz(num_qubits, depth=2):
    qc = QuantumCircuit(num_qubits)
    params = []

    for d in range(depth):
        for q in range(num_qubits):
            theta = Parameter(f"θ_{d}_{q}")
            qc.ry(theta, q)
            params.append(theta)

        for q in range(num_qubits - 1):
            qc.cz(q, q + 1)

    return qc, params
