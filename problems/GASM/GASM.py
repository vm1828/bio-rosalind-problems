"""Genome Assembly Using Reads"""

from shared.constants import PROBLEM, SOLUTION
    
def gasm_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = gasm_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

