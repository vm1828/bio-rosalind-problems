"""Inferring mRNA from Protein"""

from collections import defaultdict
from Bio.Data import CodonTable

from shared.solution import Solution

# aa_to_mRNA_codons = {
#     "A": ["GCU", "GCC", "GCA", "GCG"],
#     "C": ["UGU", "UGC"],
#     "D": ["GAU", "GAC"],
#     "E": ["GAA", "GAG"],
#     "F": ["UUU", "UUC"],
#     "G": ["GGU", "GGC", "GGA", "GGG"],
#     "H": ["CAU", "CAC"],
#     "I": ["AUU", "AUC", "AUA"],
#     "K": ["AAA", "AAG"],
#     "L": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
#     "M": ["AUG"],
#     "N": ["AAU", "AAC"],
#     "P": ["CCU", "CCC", "CCA", "CCG"],
#     "Q": ["CAA", "CAG"],
#     "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
#     "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
#     "T": ["ACU", "ACC", "ACA", "ACG"],
#     "V": ["GUU", "GUC", "GUA", "GUG"],
#     "W": ["UGG"],
#     "Y": ["UAU", "UAC"],
#     "*": ["UAA", "UAG", "UGA"],
# }


class MRNASolution(Solution):

    @staticmethod
    def algorithm(prot: str) -> int:
        """
        Calculates the total number of possible mRNA sequences that could encode a given protein,
        modulo 1,000,000.

        Args:
            prot (str): A string representing the protein sequence, with each character as an amino acid.

        Returns:
            int: The total number of possible mRNA sequences modulo 1,000,000.
        """
        # create aa_to_mRNA_codons mapping
        aa_to_mRNA_codons = defaultdict(list)
        for codon, aa in CodonTable.unambiguous_dna_by_id[1].forward_table.items():
            aa_to_mRNA_codons[aa].append(codon)

        # calculate number of possible coding sequences
        n = 1
        print(aa_to_mRNA_codons)
        for aa in prot:
            n *= len(aa_to_mRNA_codons[aa])
        n *= 3  # stop codons
        return n % 1000000

    def _parse(self) -> str:
        with open(self._input_file) as f:
            prot = f.readline().strip()
        return prot

    def _solve(self):
        result = self.algorithm(self._parsed_data)
        return str(result)


if __name__ == '__main__':
    MRNASolution()
