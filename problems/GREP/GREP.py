"""Genome Assembly with Perfect Coverage and Repeats"""

from shared.constants import PROBLEM, SOLUTION
    
def grep_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = grep_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

