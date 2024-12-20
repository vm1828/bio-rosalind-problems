"""Alignment-Based Phylogeny"""

from shared.constants import PROBLEM, SOLUTION
    
def alph_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = alph_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

