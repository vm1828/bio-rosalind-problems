"""Isolating Symbols in Alignments"""

from shared.constants import PROBLEM, SOLUTION
    
def osym_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = osym_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

