"""Introduction to Set Operations"""

from shared.constants import PROBLEM, SOLUTION
    
def seto_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = seto_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

