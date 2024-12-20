"""Overlap Alignment"""

from shared.constants import PROBLEM, SOLUTION
    
def oap_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = oap_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

