"""Quartet Distance"""

from shared.constants import PROBLEM, SOLUTION
    
def qrtd_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = qrtd_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

