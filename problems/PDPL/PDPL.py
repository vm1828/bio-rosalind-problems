"""Creating a Restriction Map"""

from shared.constants import PROBLEM, SOLUTION
    
def pdpl_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = pdpl_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

