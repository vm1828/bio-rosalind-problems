"""Wobble Bonding and RNA Secondary Structures"""

from shared.constants import PROBLEM, SOLUTION
    
def rnas_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = rnas_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

