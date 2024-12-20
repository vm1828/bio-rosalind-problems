"""Maximum Matchings and RNA Secondary Structures"""

from shared.constants import PROBLEM, SOLUTION
    
def mmch_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = mmch_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

