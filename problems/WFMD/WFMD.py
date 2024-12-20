"""The Wright-Fisher Model of Genetic Drift"""

from shared.constants import PROBLEM, SOLUTION
    
def wfmd_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = wfmd_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

