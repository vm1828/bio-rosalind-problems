"""Introduction to Pattern Matching"""

from shared.constants import PROBLEM, SOLUTION
    
def trie_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = trie_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

