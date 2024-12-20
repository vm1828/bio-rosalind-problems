"""Introduction to Random Strings"""

from shared.constants import PROBLEM, SOLUTION
    
def prob_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = prob_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

