"""Global Alignment with Constant Gap Penalty"""

from shared.constants import PROBLEM, SOLUTION
    
def gcon_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = gcon_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

