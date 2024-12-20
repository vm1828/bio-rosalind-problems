"""Creating a Distance Matrix"""

from shared.constants import PROBLEM, SOLUTION
    
def pdst_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = pdst_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

