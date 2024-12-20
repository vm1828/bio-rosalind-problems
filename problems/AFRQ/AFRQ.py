"""Counting Disease Carriers"""

from shared.constants import PROBLEM, SOLUTION
    
def afrq_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = afrq_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

