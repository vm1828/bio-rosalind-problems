"""Computing GC Content"""

from shared.constants import PROBLEM, SOLUTION
    
def gc_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = gc_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

