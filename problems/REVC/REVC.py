# Complementing a Strand of DNA

from shared.constants import PROBLEM, SOLUTION


def reverse_complement(s: str) -> str:
    """Generate reverse complement of a DNA strand

    Args:
        s (str): DNA sequence

    Returns:
        str: reverse complement of a DNA sequence
    """
    return s[::-1].translate(str.maketrans('ACGT', 'TGCA'))


# def reverse_complement(s: str) -> str:
#     complements = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
#     return ''.join(complements[i] for i in reversed(s) if i in complements)


# def reverse_complement(s: str) -> str:
#     return s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]

if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = reverse_complement(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)