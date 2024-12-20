"""Creating a Character Table"""

from shared.constants import PROBLEM, SOLUTION
    
def ctbl_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = ctbl_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

