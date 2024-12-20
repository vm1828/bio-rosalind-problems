"""Translating RNA into Protein"""

from shared.constants import PROBLEM, SOLUTION
    
def prot_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = prot_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

