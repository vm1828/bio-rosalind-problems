"""Enumerating Gene Orders"""

from shared.constants import PROBLEM, SOLUTION
    
def perm_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = perm_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

