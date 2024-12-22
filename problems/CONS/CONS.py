"""Consensus and Profile"""

from collections import defaultdict

import numpy as np
import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

from shared.solution import Solution


class CONSSolution(Solution):

    @staticmethod
    def algorithm(profile: pd.DataFrame) -> str:
        """
        Generates a consensus sequence from a profile matrix.

        To generate the profile matrix, the `profile_matrix` method can be used.

        Args:
            profile (pd.DataFrame): A DataFrame representing the profile matrix, 
                                    where each row corresponds to a nucleotide position 
                                    and each column represents a nucleotide (A, C, G, T).

        Returns:
            str: The consensus sequence, formed by selecting the most frequent nucleotide 
                at each position in the profile matrix.
        """
        consensus = ''.join([b for b in profile.idxmax(axis=1)])
        return consensus

    @staticmethod
    def profile_matrix(records: iter[SeqRecord]) -> pd.DataFrame:
        """
        Creates a profile matrix based on multiple sequence alignments.

        Args:
            records (iter[SeqRecord]): An iterator over SeqRecord objects, where each
                                    contains a sequence (string) to be used in the profile.

        Returns:
            pd.DataFrame: A pandas DataFrame representing the profile matrix, where each
                        column corresponds to a position in the sequence alignment,
                        and each row corresponds to a nucleotide (A, C, G, T) with
                        counts of occurrences at that position.
        Raises:
            ValueError: If sequences have differing lengths.
        """
        # create profile
        profile = None
        for record in records:
            sequence = record.seq
            if not profile:
                sequence_length = len(sequence)
                profile = defaultdict(
                    lambda: np.zeros(sequence_length, dtype=int))
            if len(sequence) != sequence_length:
                raise ValueError('All sequences should have the same length')
            for i in range(len(sequence)):
                profile[sequence[i]][i] += 1
        profile = pd.DataFrame.from_dict(profile)
        return profile

    def _parse(self) -> iter[SeqRecord]:
        records = SeqIO.parse(self._input_file, 'fasta')
        return records

    def _solve(self) -> str:
        profile = self.profile_matrix(self._parsed_data)
        consensus = self.algorithm(profile)
        return f"""{consensus}
A: {' '.join(profile['A'].astype(str))}
C: {' '.join(profile['C'].astype(str))}
G: {' '.join(profile['G'].astype(str))}
T: {' '.join(profile['T'].astype(str))}"""


if __name__ == '__main__':
    CONSSolution()
