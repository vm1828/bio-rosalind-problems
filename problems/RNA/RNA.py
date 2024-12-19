# Transcribing DNA into RNA

from shared.constants import PROBLEM, SOLUTION


def dna_to_rna(s: str) -> str:
    """Transcribe DNA into RNA

    Args:
        s (str): DNA sequence

    Returns:
        str: RNA sequence
    """
    return s.replace('T', 'U')


# def dna_to_rna(s: str) -> str:
#     table = str.maketrans({'T': 'U'})
#     return s.translate(table)


if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = dna_to_rna(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)
