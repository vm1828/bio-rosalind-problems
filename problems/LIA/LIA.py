"""Independent Alleles"""

from shared.constants import PROBLEM, SOLUTION
    
def lia_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = lia_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

