"""Counting Optimal Alignments"""

from shared.constants import PROBLEM, SOLUTION
    
def ctea_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = ctea_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

