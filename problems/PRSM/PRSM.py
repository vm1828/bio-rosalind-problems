"""Matching a Spectrum to a Protein"""

from shared.constants import PROBLEM, SOLUTION
    
def prsm_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = prsm_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

