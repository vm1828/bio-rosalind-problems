"""Counting DNA Nucleotides"""

from shared.solution import Solution


class DNASolution(Solution):

    @staticmethod
    def algorithm(s: str) -> tuple[int]:
        """Count DNA nucleotides

        Args:
            s (str): DNA sequence

        Returns:
            tuple[int]: counts of each nucleobase
        """
        return (s.count('A'), s.count('C'), s.count('G'), s.count('T'))

    def _solve(self) -> str:
        result = self.algorithm(self._parsed_data)
        return ' '.join([str(i) for i in result])


if __name__ == '__main__':
    DNASolution()
