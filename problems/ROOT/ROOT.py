"""Counting Rooted Binary Trees"""

from shared.constants import PROBLEM, SOLUTION
    
def root_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = root_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

