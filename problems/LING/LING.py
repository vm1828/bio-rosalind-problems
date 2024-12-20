"""Linguistic Complexity of a Genome"""

from shared.constants import PROBLEM, SOLUTION
    
def ling_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = ling_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

