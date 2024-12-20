"""Finding a Motif in DNA"""

from shared.constants import PROBLEM, SOLUTION
    
def subs_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = subs_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

