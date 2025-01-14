"""Finding a Shared Motif"""

import re

from shared.regex_patterns import FASTA_PARSE_PATTERN
from shared.solution import Solution


class LCSMSolution(Solution):

    @staticmethod
    def _shared_motif(seq_0: str, seqs: list[str], start: int, length: int) -> tuple[int, str]:
        """Find the first motif of a given length in the first sequence that is present in all other sequences."""
        for i in range(start, len(seq_0)-length+1):
            motif = seq_0[i:i+length]
            if all(motif in seq for seq in seqs):
                return (i, motif)
        return (-1, '')

    @staticmethod
    def algorithm(seqs: list[str]) -> str:
        """
        Find the longest common motif (substring) across multiple sequences (strings) using binary search.

        Args:
            seqs (list[str]): A list of strings to find the longest common substring.

        Returns:
            str: The longest common substring found across all the strings.
        """
        seq_0 = seqs.pop()
        l, r = 0, len(seq_0)
        start = 0
        longest_motif = ''
        while l < r:
            m = (l + r) // 2
            i, motif = __class__._shared_motif(seq_0, seqs, start, m)
            if i > -1:  # Motif found
                start = i
                longest_motif = motif
                l = m + 1  # Search in the larger half
            else:
                r = m  # Search in the smaller half
        return longest_motif

    def _parse(self) -> list[str]:
        with open(self._input_file) as f:
            seqs = FASTA_PARSE_PATTERN.findall(f.read().replace("\n", ""))
        return seqs

    def _solve(self) -> str:
        return self.algorithm(self._parsed_data)


# def find_shared_motif_naive(seqs: list[str]) -> str:
#     shortest_seq = min(seqs, key=len)
#     for window_len in range(len(shortest_seq), 0, -1):
#         for i in range(len(shortest_seq)-window_len+1):
#             motif = shortest_seq[i:i+window_len]
#             if all(motif in seq for seq in seqs):
#                 return motif
#     return ''


if __name__ == '__main__':
    LCSMSolution()
