"""Comparing Spectra with the Spectral Convolution"""

from shared.constants import PROBLEM, SOLUTION
    
def conv_soln():
    ...

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = conv_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)

