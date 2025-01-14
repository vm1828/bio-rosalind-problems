"""Enumerating k-mers Lexicographically"""

import itertools
from shared.solution import Solution


class LEXFSolution(Solution):

    @staticmethod
    def algorithm(symbols: list[str], k: int) -> list[str]:
        """
        Generates all lexicographically ordered combinations of elements from the input symbols, repeated k times.

        Args:
            symbols (list[str]): A list of symbols to use in combinations.
            k (int): The number of repetitions for each combination.

        Returns:
            list[str]: A list of all possible combinations as strings.
        """
        symbols = sorted(symbols)
        return [''.join(i) for i in itertools.product(symbols, repeat=k)]

    def _parse(self) -> tuple[list[str], int]:
        with open(self._input_file) as f:
            symbols = f.readline().strip().split(' ')
            k = int(f.readline().strip())
        return symbols, k

    def _solve(self):
        kmers = self.algorithm(*self._parsed_data)
        return '\n'.join(kmers)


if __name__ == '__main__':
    LEXFSolution()
