"""Transitions and Transversions"""

from shared.constants import PROBLEM, SOLUTION
    
def tran_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = tran_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

