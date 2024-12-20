"""Phylogeny Comparison with Split Distance"""

from shared.constants import PROBLEM, SOLUTION
    
def sptd_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = sptd_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

