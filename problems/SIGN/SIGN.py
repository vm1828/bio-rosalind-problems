"""Enumerating Oriented Gene Orderings"""

from shared.constants import PROBLEM, SOLUTION
    
def sign_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = sign_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

