"""Local Alignment with Scoring Matrix"""

from shared.constants import PROBLEM, SOLUTION
    
def loca_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = loca_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

