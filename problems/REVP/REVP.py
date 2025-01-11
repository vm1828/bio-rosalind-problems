"""Locating Restriction Sites"""

from shared.solution import Solution


class REVPSolution(Solution):

    @staticmethod
    def algorithm(
        dna_5_3: str,
        min_len: int = 4,
        max_len: int = 12
    ) -> list[tuple[int, int]]:
        """Finds palindromic sequences within a DNA strand.

        Args:
            dna_5_3 (str): The 5' to 3' direction DNA sequence.
            min_len (int, optional): Minimum length of palindromic sequences. Defaults to 4.
            max_len (int, optional): Maximum length of palindromic sequences. Defaults to 12.

        Returns:
            list[tuple[int, int]]: A list of tuples with 0-based start and end indices of palindromic sequences.
        """
        dna_len = len(dna_5_3)
        dna_3_5 = dna_5_3.translate(str.maketrans('ACGT', 'TGCA'))

        palindromes = []
        length = max_len
        for i in range(dna_len-3):
            while (length >= min_len):
                s1 = dna_5_3[i:i+length]
                s2 = dna_3_5[i:i+length][::-1]
                if s1 == s2:
                    # End index is inclusive, adjusted for 0-based indexing
                    palindromes.append((i, i+length-1))
                    break
                length -= 1
            length = max_len if (dna_len-i > 12) else (dna_len-i-1)
        return palindromes

    def _parse(self) -> str:
        with open(self._input_file) as f:
            next(f)
            dna_5_3 = f.read().replace('\n', '')
        return dna_5_3

    def _solve(self) -> str:
        palindromes = self.algorithm(self._parsed_data)
        return '\n'.join([f'{i1+1} {i2-i1+1}' for i1, i2 in palindromes])


if __name__ == '__main__':
    REVPSolution()
