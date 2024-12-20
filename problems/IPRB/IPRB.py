"""Mendel's First Law"""

from shared.constants import PROBLEM, SOLUTION
    
def iprb_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = iprb_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

