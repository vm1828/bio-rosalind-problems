"""Finding the Longest Multiple Repeat"""

from shared.constants import PROBLEM, SOLUTION
    
def lrep_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = lrep_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

