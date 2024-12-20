"""Assessing Assembly Quality with N50 and N75"""

from shared.constants import PROBLEM, SOLUTION
    
def asmq_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = asmq_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

