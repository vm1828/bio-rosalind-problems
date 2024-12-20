"""The Founder Effect and Genetic Drift"""

from shared.constants import PROBLEM, SOLUTION
    
def foun_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = foun_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

