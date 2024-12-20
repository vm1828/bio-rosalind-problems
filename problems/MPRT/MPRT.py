"""Finding a Protein Motif"""

from shared.constants import PROBLEM, SOLUTION
    
def mprt_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = mprt_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

