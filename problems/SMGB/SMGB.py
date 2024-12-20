"""Semiglobal Alignment"""

from shared.constants import PROBLEM, SOLUTION
    
def smgb_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = smgb_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

