"""Calculating Protein Mass"""

# from Bio.SeqUtils import molecular_weight

from shared.solution import Solution


monoisotopic_mass_table = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}


class PRTMSolution(Solution):

    @staticmethod
    def algorithm(seq: str) -> float:
        """Calculates and returns the monoisotopic mass of the given sequence.

        Args:
            seq (str): A string representing the sequence of amino acids.

        Returns:
            float: The calculated monoisotopic mass, rounded to 3 decimal places.
        """
        # # different result
        # return round(molecular_weight(seq, seq_type='protein', monoisotopic=True), 3)
        return round(sum(monoisotopic_mass_table[i] for i in seq), 3)

    def _parse(self) -> str:
        with open(self._input_file) as f:
            seq = f.readline().strip()
        return seq

    def _solve(self) -> str:
        return str(self.algorithm(self._parsed_data))


if __name__ == '__main__':
    PRTMSolution()
