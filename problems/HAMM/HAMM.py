"""Counting Point Mutations"""

from shared.constants import PROBLEM, SOLUTION
    
def hamm_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = hamm_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

