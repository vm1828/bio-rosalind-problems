"""Finding a Shared Motif"""

from shared.constants import PROBLEM, SOLUTION
    
def lcsm_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = lcsm_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

