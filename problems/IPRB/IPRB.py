"""Mendel's First Law"""

import math
from shared.solution import Solution


class IPRBSolution(Solution):

    @staticmethod
    def algorithm(AA: int, Aa: int, aa: int) -> float:
        """
        Calculates the probability of a favorable genetic pairing.

        The method computes the proportion of favorable pairs (where the genetic combination
        results in a specific genetic trait) relative to the total possible pairs, based on 
        counts of three genotypes (AA, Aa, aa).

        Args:
            AA (int): The count of homozygous dominant (AA) individuals.
            Aa (int): The count of heterozygous (Aa) individuals.
            aa (int): The count of homozygous recessive (aa) individuals.

        Returns:
            float: The probability of a favorable genetic pairing, rounded to 5 decimal places.
        """
        total = AA+Aa+aa
        total_pairs = total*(total-1)/2

        # favorable pairs
        AA_AA = math.comb(AA, 2) if AA >= 2 else 0
        AA_Aa = AA*Aa
        AA_aa = AA*aa
        Aa_Aa = (math.comb(Aa, 2) if Aa >= 2 else 0)*0.75
        Aa_aa = Aa*aa*0.5
        favorable_pairs = AA_AA + AA_Aa + AA_aa + Aa_Aa + Aa_aa

        return round(favorable_pairs/total_pairs, 5)

    def _parse(self) -> tuple[int]:
        with open(self._input_file) as f:
            AA, Aa, aa = (int(i) for i in f.read().strip().split())
        return AA, Aa, aa

    def _solve(self) -> str:
        return str(self.algorithm(*self._parsed_data))


if __name__ == '__main__':
    IPRBSolution()
