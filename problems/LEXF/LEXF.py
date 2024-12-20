"""Enumerating k-mers Lexicographically"""

from shared.constants import PROBLEM, SOLUTION
    
def lexf_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = lexf_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

