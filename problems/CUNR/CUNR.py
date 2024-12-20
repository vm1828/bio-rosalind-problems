"""Counting Unrooted Binary Trees"""

from shared.constants import PROBLEM, SOLUTION
    
def cunr_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = cunr_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

