"""Counting DNA Nucleotides"""

from shared.constants import PROBLEM, SOLUTION


def dna_soln(s: str) -> tuple[int]:
    """Count 

    Args:
        s (str): DNA sequence

    Returns:
        tuple[int]: counts of each nucleobase
    """
    return (s.count('A'), s.count('C'), s.count('G'), s.count('T'))


if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = ' '.join([str(i) for i in dna_soln(s)])
    with open(SOLUTION, 'w') as f:
        f.write(solution)
