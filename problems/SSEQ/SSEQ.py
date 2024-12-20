"""Finding a Spliced Motif"""

from shared.constants import PROBLEM, SOLUTION
    
def sseq_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = sseq_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

