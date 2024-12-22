"""Counting Point Mutations"""

from shared.solution import Solution


class HAMMSolution(Solution):

    @staticmethod
    def algorithm(s1: str, s2: str) -> int:
        """
        Computes the Hamming distance between two sequences of equal length.
        The Hamming distance is the number of positions at which the corresponding characters are different.

        Args:
            s1 (str): The first string for comparison.
            s2 (str): The second string for comparison.

        Returns:
            int: The Hamming distance between the two strings.

        Raises:
            ValueError: If the input strings have different lengths.
        """
        if len(s1) != len(s2):
            raise ValueError("Strings must be of the same length.")
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    def _parse(self) -> tuple[str, str]:
        with open(self._input_file) as f:
            s1 = f.readline().strip()
            s2 = f.readline().strip()
            assert len(s1) == len(s2)
        return s1, s2

    def _solve(self) -> str:
        return str(self.algorithm(*self._parsed_data))


if __name__ == '__main__':
    HAMMSolution()
