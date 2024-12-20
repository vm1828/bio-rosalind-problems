"""Maximizing the Gap Symbols of an Optimal Alignment"""

from shared.constants import PROBLEM, SOLUTION
    
def mgap_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = mgap_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

