"""Open Reading Frames"""

from shared.constants import PROBLEM, SOLUTION
    
def orf_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = orf_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

