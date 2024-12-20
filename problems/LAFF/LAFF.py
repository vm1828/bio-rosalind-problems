"""Local Alignment with Affine Gap Penalty"""

from shared.constants import PROBLEM, SOLUTION
    
def laff_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = laff_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

