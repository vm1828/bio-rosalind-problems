"""Finding a Shared Spliced Motif"""

from shared.constants import PROBLEM, SOLUTION
    
def lcsq_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = lcsq_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

