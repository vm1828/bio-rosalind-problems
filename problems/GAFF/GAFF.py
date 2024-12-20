"""Global Alignment with Scoring Matrix and Affine Gap Penalty"""

from shared.constants import PROBLEM, SOLUTION
    
def gaff_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = gaff_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

