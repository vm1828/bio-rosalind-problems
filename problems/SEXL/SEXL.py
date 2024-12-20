"""Sex-Linked Inheritance"""

from shared.constants import PROBLEM, SOLUTION
    
def sexl_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = sexl_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

