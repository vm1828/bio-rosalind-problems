"""Multiple Alignment"""

from shared.constants import PROBLEM, SOLUTION
    
def mult_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = mult_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

