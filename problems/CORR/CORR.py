"""Error Correction in Reads"""

from shared.constants import PROBLEM, SOLUTION
    
def corr_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = corr_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

