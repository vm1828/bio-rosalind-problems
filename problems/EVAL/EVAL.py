"""Expected Number of Restriction Sites"""

from shared.constants import PROBLEM, SOLUTION
    
def eval_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = eval_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

