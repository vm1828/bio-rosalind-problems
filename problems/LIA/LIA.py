"""Independent Alleles"""

import math
from shared.solution import Solution


class LIASolution(Solution):

    @staticmethod
    def algorithm(generations: int, at_least: int) -> float:
        """
        Calculates the probability of having at least a specified number of 
        AaBb offspring in a given number of generations, based on Mendelian inheritance.

        Args:
            generations (int): The number of generations.
            at_least (int): The minimum number of AaBb offspring to consider.

        Returns:
            float: The probability of having at least the specified number of AaBb offspring.
        """
        prob_AaBb = 0.25
        total_offsprings = 2**generations
        probs = []
        for k in range(at_least, total_offsprings+1):
            # probability of exactly k AaBb offsprings
            nCk = math.comb(total_offsprings, k)
            prob_k = nCk * (prob_AaBb**k) * \
                ((1-prob_AaBb)**(total_offsprings-k))
            probs.append(prob_k)
        return round(sum(probs), 3)

    def _parse(self) -> tuple[int, int]:
        with open(self._input_file) as f:
            generations, at_least = [int(i) for i in f.readline().split()]
        return generations, at_least

    def _solve(self) -> str:
        return str(self.algorithm(*self._parsed_data))


if __name__ == '__main__':
    LIASolution()
