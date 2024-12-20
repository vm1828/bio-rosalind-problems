"""Calculating Expected Offspring"""

from shared.constants import PROBLEM, SOLUTION
    
def iev_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = iev_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

