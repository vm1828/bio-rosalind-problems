"""Encoding Suffix Trees"""

from shared.constants import PROBLEM, SOLUTION
    
def suff_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = suff_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

