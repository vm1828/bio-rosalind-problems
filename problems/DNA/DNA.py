"""Counting DNA Nucleotides"""

from shared.solution import Solution


class DNASolution(Solution):

    @staticmethod
    def algorithm(s: str) -> dict[str, int]:
        """Counts the occurrences of each nucleotide in a DNA sequence.

        Args:
            s (str): The DNA sequence.

        Returns:
            dict[str, int]: A dictionary where keys are nucleotides ('A', 'C', 'G', 'T') and 
                            values are their respective counts in the sequence.
        """
        counts = {}
        for b in 'ACGT':
            counts[b] = s.count(b)
        return counts

    def _solve(self) -> str:
        solution = self.algorithm(self._parsed_data)
        return ' '.join([str(i) for i in solution.values()])


if __name__ == '__main__':
    DNASolution()
