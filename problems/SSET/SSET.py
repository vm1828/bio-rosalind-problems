"""Counting Subsets"""

from shared.constants import PROBLEM, SOLUTION
    
def sset_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = sset_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

