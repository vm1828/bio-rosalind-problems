"""Counting Phylogenetic Ancestors"""

from shared.constants import PROBLEM, SOLUTION
    
def inod_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = inod_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

