"""Open Reading Frames"""

from Bio.Data import CodonTable

from shared.solution import Solution


class ORFSolution(Solution):

    @staticmethod
    def find_orfs(dna: str) -> list[tuple[int, int]]:
        """
        Finds open reading frames (ORFs) in the given DNA sequence.

        Args:
            dna (str): DNA sequence consisting of nucleotides ('A', 'T', 'G', 'C').

        Returns:
            list[tuple[int, int]]: A list of tuples where each tuple (start, stop)
                                represents the 0-indexed positions of the start codon ('ATG')
                                and the stop codon ('TAA', 'TAG', 'TGA').
                                The indices are inclusive for the start codon
                                and exclusive for the stop codon.
        """
        orfs = []
        start = dna.find('ATG')
        # For each start codon find corresponding stop codon
        while start != -1:
            stop = next((i for i in range(start, len(dna) - 2, 3)
                        if dna[i:i+3] in ["TAA", "TAG", "TGA"]), -1)
            if stop != -1:
                # # omit last letter of stop codon
                # orfs.append(dna[start:stop+2])
                orfs.append((start, stop))
            start = dna.find('ATG', start+1)
        return orfs

    @staticmethod
    def algorithm(dna: str) -> tuple[str, ...]:
        """
        Identifies all unique amino acid sequences encoded by open reading frames (ORFs) 
        in a DNA sequence and its reverse complement.

        Args:
            dna (str): DNA sequence.

        Returns:
            tuple[str, ...]: A tuple of unique amino acid sequences translated from all 
                            ORFs found in the DNA sequence and its reverse complement.
        """
        # # regex does not find overlapping sequences !!!
        # pattern = r"ATG(?:[ATGC]{3})*?(?:TAA|TAG|TGA)"
        reverse_complement = dna[::-1].translate(str.maketrans('ACGT', 'TGCA'))
        dna_to_aa = CodonTable.standard_dna_table.forward_table

        dna_orfs = ORFSolution.find_orfs(dna)
        reverse_complement_orfs = ORFSolution.find_orfs(reverse_complement)
        orfs = {
            dna: dna_orfs,
            reverse_complement: reverse_complement_orfs
        }

        aa_seqs = []
        for seq, orfs in orfs.items():
            for start, stop in orfs:
                orf = seq[start:stop]
                aa_seq = [dna_to_aa.get(
                    orf[j:j+3]) for j in range(0, len(orf), 3) if dna_to_aa.get(orf[j:j+3])]
                aa_seqs.append(''.join(aa_seq))
        return tuple(set(aa_seqs))

    def _parse(self) -> str:
        with open(self._input_file) as f:
            next(f)
            dna = f.read().replace('\n', '')
        return dna

    def _solve(self):
        return '\n'.join(self.algorithm(self._parsed_data))


if __name__ == '__main__':
    ORFSolution()
