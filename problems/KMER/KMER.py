"""k-Mer Composition"""

from shared.constants import PROBLEM, SOLUTION
    
def kmer_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = kmer_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

