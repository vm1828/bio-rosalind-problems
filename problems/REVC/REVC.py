"""Complementing a Strand of DNA"""

from shared.solution import Solution


class REVCSolution(Solution):

    @staticmethod
    def algorithm(s: str) -> str:
        """Generates the reverse complement of a DNA sequence.

        Args:
            s (str): DNA sequence.

        Returns:
            str: The reverse complement of the input DNA sequence.
        """
        return s[::-1].translate(str.maketrans('ACGT', 'TGCA'))


# def revc_soln(s: str) -> str:
#     complements = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
#     return ''.join(complements[i] for i in reversed(s) if i in complements)


# def revc_soln(s: str) -> str:
#     return s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]

if __name__ == '__main__':
    REVCSolution()
