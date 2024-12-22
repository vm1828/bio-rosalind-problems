"""Transcribing DNA into RNA"""

from shared.solution import Solution


class RNASolution(Solution):

    @staticmethod
    def algorithm(s: str) -> str:
        """
        Transcribes a DNA sequence into an RNA sequence by replacing thymine (T) with uracil (U).

        Args:
            s (str): The DNA sequence to be transcribed.

        Returns:
            str: The corresponding RNA sequence.
        """
        return s.replace('T', 'U')


# def rna_soln(s: str) -> str:
#     table = str.maketrans({'T': 'U'})
#     return s.translate(table)


if __name__ == '__main__':
    RNASolution()
