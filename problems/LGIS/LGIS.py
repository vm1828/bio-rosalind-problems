"""Longest Increasing Subsequence"""

from shared.constants import PROBLEM, SOLUTION
    
def lgis_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = lgis_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

