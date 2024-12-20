"""Speeding Up Motif Finding"""

from shared.constants import PROBLEM, SOLUTION
    
def kmp_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = kmp_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

