"""Genome Assembly with Perfect Coverage"""

from shared.constants import PROBLEM, SOLUTION
    
def pcov_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = pcov_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

