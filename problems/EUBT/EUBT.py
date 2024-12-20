"""Enumerating Unrooted Binary Trees"""

from shared.constants import PROBLEM, SOLUTION
    
def eubt_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = eubt_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

