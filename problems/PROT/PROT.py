"""Translating RNA into Protein"""

from shared.constants import PROBLEM, SOLUTION
from Bio.Seq import Seq
# from Bio.Data import CodonTable


def prot_soln(s: str) -> str:
    """Translates an RNA sequence to a protein sequence

    Args:
        s (str): RNA sequence

    Returns:
        str: Protein sequence
    """
    rna_seq = Seq(s)
    prot_seq = rna_seq.translate(to_stop=True)
    return prot_seq


# def prot_soln(s: str) -> str:
#   codon_table = CodonTable.standard_rna_table.forward_table
#   start = s.find('AUG')
#   protein_seq = []
#   for i in range(start, len(s), 3):
#     codon = s[i:i+3]
#     if codon in ['UAA', 'UAG', 'UGA']:
#       break
#     protein_seq.append(codon_table[codon])
#   return ''.join(protein_seq)


if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.read().strip()
    solution = prot_soln(s)
    with open(SOLUTION, 'w') as f:
        f.write(solution)
