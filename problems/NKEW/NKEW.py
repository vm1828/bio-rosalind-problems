"""Newick Format with Edge Weights"""

from shared.constants import PROBLEM, SOLUTION
    
def nkew_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = nkew_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

