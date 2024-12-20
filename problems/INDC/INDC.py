"""Independent Segregation of Chromosomes"""

from shared.constants import PROBLEM, SOLUTION
    
def indc_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = indc_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

