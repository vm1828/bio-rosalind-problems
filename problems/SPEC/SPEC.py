"""Inferring Protein from Spectrum"""

from shared.constants import PROBLEM, SOLUTION
    
def spec_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = spec_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

