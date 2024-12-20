"""Creating a Character Table from Genetic Strings"""

from shared.constants import PROBLEM, SOLUTION
    
def cstr_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = cstr_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

