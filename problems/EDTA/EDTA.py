"""Edit Distance Alignment"""

from shared.constants import PROBLEM, SOLUTION
    
def edta_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = edta_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

