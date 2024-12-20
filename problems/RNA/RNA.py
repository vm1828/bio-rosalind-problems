"""Transcribing DNA into RNA"""

from shared.constants import PROBLEM, SOLUTION


def rna_soln(s: str) -> str:
    """Transcribe DNA into RNA

    Args:
        s (str): DNA sequence

    Returns:
        str: RNA sequence
    """
    return s.replace('T', 'U')


# def rna_soln(s: str) -> str:
#     table = str.maketrans({'T': 'U'})
#     return s.translate(table)


if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read()
    solution = rna_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)
