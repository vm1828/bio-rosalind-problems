"""Fixing an Inconsistent Character Set"""

from shared.constants import PROBLEM, SOLUTION
    
def cset_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = cset_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

