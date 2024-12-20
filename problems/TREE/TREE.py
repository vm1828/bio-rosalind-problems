"""Completing a Tree"""

from shared.constants import PROBLEM, SOLUTION
    
def tree_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = tree_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

