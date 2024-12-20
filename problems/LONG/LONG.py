"""Genome Assembly as Shortest Superstring"""

from shared.constants import PROBLEM, SOLUTION
    
def long_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = long_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

