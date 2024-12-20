"""Introduction to Alternative Splicing"""

from shared.constants import PROBLEM, SOLUTION
    
def aspc_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = aspc_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

