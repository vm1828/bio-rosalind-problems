"""Reversal Distance"""

from shared.constants import PROBLEM, SOLUTION
    
def rear_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = rear_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

