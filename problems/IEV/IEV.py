"""Calculating Expected Offspring"""

from shared.solution import Solution


class IEVSolution(Solution):

    @staticmethod
    def algorithm(
        n_pairs: tuple[int, ...],
        probabilities: tuple[float, ...],
        n_offsprings: int = 2
    ) -> float:
        """
        Calculate the expected number of offspring of a specific type (e.g. dominant).

        Args:
            n_pairs (tuple[int, ...]): Number of genotype pairs (e.g. 'AA-AA', 'AA-Aa', 'AA-aa', ...).
            probabilities (tuple[float, ...]): Probabilities of having offspring of this type for each genotype pair.
            n_offsprings (int, optional): Number of offspring per pair. Defaults to 2.

        Returns:
            float: Expected number of offspring of the specified type.
        """
        return sum(n * prob * n_offsprings for n, prob in zip(n_pairs, probabilities))

    def _parse(self) -> tuple[int, ...]:
        with open(self._input_file) as f:
            # pairs = ['AA-AA', 'AA-Aa', 'AA-aa', 'Aa-Aa', 'Aa-aa', 'aa-aa']
            n_pairs = tuple(int(i) for i in f.readline().split())
        return n_pairs

    def _solve(self) -> str:
        dominant_offspring_prob = (1.0, 1.0, 1.0, 0.75, 0.5, 0.0)
        return str(self.algorithm(self._parsed_data, dominant_offspring_prob))


if __name__ == '__main__':
    IEVSolution()
