"""Overlap Graphs"""

from collections import defaultdict
import re
from shared.models import FastaRecord
from shared.solution import Solution


class GRPHSolution(Solution):

    @staticmethod
    def algorithm(records: list[FastaRecord], k: int = 3) -> list[tuple[int, int]]:
        """
        Finds pairs of sequences from the provided records that have matching k-mer prefixes and suffixes.

        This algorithm creates an adjacency list based on the first and last k characters of the sequences.
        It identifies pairs of sequences where the suffix of one sequence matches the prefix of another.

        Args:
            records (list[FastaRecord]): A list of `FastaRecord` objects, where each contains an identifier
                                        and a sequence string.
            k (int, optional): The length of the prefix and suffix to compare. Defaults to 3.

        Returns:
            list[tuple[int, int]]: A list of pairs of sequence identifiers (represented as integers) 
                                    that share matching prefixes and suffixes.
        """

        # Create adjacency list
        pairs = []
        prefixes = defaultdict(list)

        # Build prefix map
        for id, seq in records:
            prefixes[seq[:k]].append(id)

        # Find matching suffixes and prefixes
        for id1, seq1 in records:
            suffix = seq1[-k:]
            for id2 in prefixes[suffix]:
                if id2 != id1:
                    pairs.append((id1, id2))

        return pairs

    def _parse(self) -> list[FastaRecord]:
        pattern = re.compile(
            r'>(?P<label>Rosalind_\d{4})\s*(?P<bases>[ACGT\s]+)')
        with open(self._input_file) as f:
            records = pattern.findall(f.read().replace("\n", ""))
        return records

    def _solve(self) -> str:
        result = ""
        pairs = self.algorithm(self._parsed_data)
        for pair in pairs:
            result += f'{pair[0]} {pair[1]}\n'
        return result.rstrip()


if __name__ == '__main__':
    GRPHSolution()
