"""Inferring Genotype from a Pedigree"""

from shared.constants import PROBLEM, SOLUTION
    
def mend_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = mend_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

