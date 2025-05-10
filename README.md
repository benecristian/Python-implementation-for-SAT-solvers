# SAT Solver Comparison (Resolution, DP, DPLL)

This repository contains three Python implementations of classic SAT solving algorithms:

- `resolution.py` – Resolution-based inference method  
- `dp.py` – Davis–Putnam (DP) algorithm  
- `dpll.py` – Davis–Putnam–Logemann–Loveland (DPLL) algorithm  

It also includes a few test files in CNF format (`test1cnf.txt` to `test6cnf.txt`) for checking how each solver works on small examples.

## How it Works

Each solver file contains a function that takes a CNF formula (as a list of clauses) and returns whether the formula is satisfiable (SAT) or not (UNSAT). You can load a CNF file and test all solvers in the same script.

### Example usage in Python

```python
from resolution import resolution_solver
from dp import dp_solver
from dpll import dpll

def load_cnf_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line and not line.startswith(('c', 'p'))]
        return [list(map(int, line.split()))[:-1] for line in lines]

cnf = load_cnf_file("test1cnf.txt")

print("Resolution:", resolution_solver(cnf))
print("DP:", dp_solver(cnf))
print("DPLL:", dpll(cnf))
