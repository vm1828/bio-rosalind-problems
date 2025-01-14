"""RNA Splicing"""

import re
from problems.PROT.PROT import PROTSolution
from shared.regex_patterns import FASTA_PARSE_PATTERN
from shared.solution import Solution


class SPLCSolution(Solution):

    @staticmethod
    def algorithm(dna: str, introns: list[str]) -> str:
        """
        Removes introns from a DNA sequence.

        Args:
            dna (str): The DNA sequence as a string.
            introns (list[str]): A list of intron sequences to be removed from the DNA.

        Returns:
            str: The DNA sequence with all introns removed.
        """
        for intron in introns:
            dna = dna.replace(intron, '')
        # dna = ''.join(dna.split(intron))
        return dna

    def _parse(self) -> tuple[str, list[str]]:
        with open(self._input_file) as f:
            records = FASTA_PARSE_PATTERN.findall(f.read().replace("\n", ""))
            dna = records[0]
            introns = records[1:]
        return dna, introns

    def _solve(self) -> str:
        spliced_rna = self.algorithm(*self._parsed_data)
        aa_seq = PROTSolution.algorithm(spliced_rna)
        return aa_seq


if __name__ == '__main__':
    SPLCSolution()
