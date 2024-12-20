"""Inferring mRNA from Protein"""

from shared.constants import PROBLEM, SOLUTION
    
def mrna_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = mrna_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

