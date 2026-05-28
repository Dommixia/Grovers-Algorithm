# Grover's Algorithm Simulation

This project provides a Python simulation of Grover's Algorithm, a quantum algorithm that finds with high probability the unique input to a black box function that produces a particular output value. It provides a quadratic speedup over classical linear search.
Do Note that we achieved this algorithm through a classical computer doing matrix multiplications mathematically. This leads to the algorithm being only slightly faster than a regular classical search
## Project Structure

- `main.py`: The core implementation of Grover's Algorithm using NumPy for state vector simulation.
- `requirements.txt`: Project dependencies.

## Mathematical Foundation

Grover's algorithm works in a Hilbert space of dimension $N = 2^n$, where $n$ is the number of qubits. The algorithm consists of four main steps:

1.  **Initialization**: Prepare a uniform superposition of all basis states:
    $$|s\rangle = H^{\otimes n} |0\rangle = \frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle$$
2.  **Oracle ($U_\omega$)**: Mark the target item by flipping its phase.
3.  **Diffusion Operator ($U_s$)**: Amplify the probability amplitude of the marked item.
4.  **Measurement**: Repeat steps 2 and 3 approximately $\frac{\pi}{4}\sqrt{N}$ times and measure the state.

### The Oracle ($U_\omega$)

The Oracle is a "black box" operation that recognizes the solution. Mathematically, for a target index $\omega$, it is defined as:
$$U_\omega |x\rangle = \begin{cases} -|x\rangle & \text{if } x = \omega \\ |x\rangle & \text{if } x \neq \omega \end{cases}$$
In this simulation, it is represented as an identity matrix where the diagonal element at the `target_index` is $-1$.

### The Diffusion Operator ($U_s$)

The diffusion operator, also known as the "Grover diffusion operator" or "inversion about the mean," redirects the amplitudes towards the target state. It is defined as:
$$U_s = 2|s\rangle\langle s| - I$$
Where $|s\rangle$ is the uniform superposition state. Geometrically, this operator reflects the state vector about the mean amplitude. Since the Oracle flipped the phase of the target, its amplitude is now negative (far from the mean). The diffusion operator then flips everything about the mean, significantly increasing the target's amplitude while slightly decreasing the others.

## Implementation Details

The simulation uses **NumPy** to handle:
- **State Vectors**: Represented as a $2^n$ complex array.
- **Kronecker Products**: Used to construct multi-qubit gates (like the Hadamard transform).
- **Matrix Multiplication**: To apply the Oracle and Diffusion operators.

### Complexity Comparison

| Search Method | Average Complexity |
| :--- | :--- |
| **Classical Search** | $O(N)$ |
| **Grover's Algorithm** | $O(\sqrt{N})$ |

## Sample Output

```
No of elements in dataset: 1024
Target At index: 552
------------------------------------------------------------
Classical Search 
Classical search time: 6.180000491440296e-05
Classical Computer found index: 552
------------------------------------------------------------
Quantum Search
Iteration count: 25
Quantum search time: 0.033005699981004
Quantum Computer found index: 552
------------------------------------------------------------
Classical iterations: 512 average
Quantum iterations: 25
Speedup factor: 20.5x
```

## Getting Started

### Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
### Running the Simulation

Execute the main script:
```bash
python main.py
```

The script will:
1. Generate a random dataset of $2^{10}$ (1024) elements.
2. Insert a target value at a random index.
3. Perform a classical search.
4. Perform the Quantum search simulation.
5. Compare the results and execution times.