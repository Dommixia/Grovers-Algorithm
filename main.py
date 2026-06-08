import numpy as np
import time

n_qubits = 10
N = 2**n_qubits

dataset = np.random.uniform(10, 100, N)
target_index = np.random.randint(0, N)
target_value = 115 #outisde the dataset range
dataset[target_index] = target_value # To ensure no duplicates are found
print(f"No of elements in dataset: {N}")
print(f"Target At index: {target_index}")
print("------------------------------------------------------------")
print("Classical Search ")
# Classical Search
start = time.perf_counter()
found_index = -1

for i in range(len(dataset)):
    if dataset[i] == target_value:
        found_index = i
        break
end = time.perf_counter()
classical_time = end - start

print(f"Classical search time: {classical_time}s")
print(f"Classical Computer found index: {found_index}")

print("------------------------------------------------------------")
print("Quantum Search")
state = np.zeros(N, dtype=complex)
state[0] = 1
H = np.array([[1,1], [1,-1]], dtype = complex)/np.sqrt(2)
I = np.eye(2, dtype=complex)

startQ = time.perf_counter()

def hadamard_all(n_qubits):
    result = H
    for _ in range(n_qubits - 1):
        result = np.kron(result, H)
    return result

H_all = hadamard_all(n_qubits)
state = H_all @ state

oracle = np.eye(N, dtype=float)
oracle[target_index, target_index] = -1

psi = np.ones(N, dtype=float) / np.sqrt(N)
diffusion = 2 * np.outer(psi, psi.conj()) - np.eye(N, dtype=complex)

iterations = int(np.round(np.pi/4 * np.sqrt(N)))
print(f"Iteration count: {iterations}")

for i in range(iterations):
    state[target_index] *= -1
    mean_amplitude = np.mean(state)
    state = 2 * mean_amplitude - state
    probs = np.abs(state) ** 2

qindex = np.argmax(probs) #Index found by quantum search

end = time.perf_counter()
quantum_time = end - startQ

print(f"Quantum search time: {quantum_time}s")
print(f"Quantum Computer found index: {qindex}")
print("------------------------------------------------------------")

print(f"Classical iterations: {N//2} average")
print(f"Quantum iterations: {iterations}")
print(f"Speedup factor: {(N//2) / iterations:.1f}x")