"""Wright-Fisher's Expected Behavior"""

from shared.constants import PROBLEM, SOLUTION
    
def ebin_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = ebin_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

