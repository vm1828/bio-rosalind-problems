"""Perfect Matchings and RNA Secondary Structures"""

from shared.constants import PROBLEM, SOLUTION
    
def pmch_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = pmch_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

