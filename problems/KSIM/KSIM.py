"""Finding All Similar Motifs"""

from shared.constants import PROBLEM, SOLUTION
    
def ksim_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = ksim_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

