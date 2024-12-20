"""Inferring Peptide from Full Spectrum"""

from shared.constants import PROBLEM, SOLUTION
    
def full_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = full_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

