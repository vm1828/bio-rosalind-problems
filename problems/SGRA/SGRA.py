"""Using the Spectrum Graph to Infer Peptides"""

from shared.constants import PROBLEM, SOLUTION
    
def sgra_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = sgra_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

