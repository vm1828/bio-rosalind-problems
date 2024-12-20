"""Mortal Fibonacci Rabbits"""

from shared.constants import PROBLEM, SOLUTION
    
def fibd_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = fibd_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

