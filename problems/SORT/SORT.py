"""Sorting by Reversals"""

from shared.constants import PROBLEM, SOLUTION
    
def sort_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = sort_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

