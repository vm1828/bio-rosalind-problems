"""Identifying Reversing Substitutions"""

from shared.constants import PROBLEM, SOLUTION
    
def rsub_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = rsub_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

