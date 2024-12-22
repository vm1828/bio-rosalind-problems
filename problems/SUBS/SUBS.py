"""Finding a Motif in DNA"""

# import re
from shared.solution import Solution


class SUBSSolution(Solution):

    @staticmethod
    def algorithm(s: str, substr: str) -> list[int]:
        """
        Finds all occurrences of a substring in a string and returns their 1-based indices.

        This method searches for all instances of the substring `substr` within the string `s` 
        and returns a list of the 1-based starting positions of each match.

        Args:
            s (str): The string.
            substr (str): The substring to find within `s`.

        Returns:
            list[int]: A list of 1-based indices where the substring `substr` occurs in the string `s`.
        """
        matches = []
        i = s.find(substr)
        while i != -1:
            matches.append(i+1)
            i = s.find(substr, i+1)
        return matches

    def _parse(self) -> tuple[str, str]:
        with open(self._input_file) as f:
            s = f.readline().rstrip()
            substr = f.readline().rstrip()
        return s, substr

    def _solve(self) -> str:
        matches = self.algorithm(*self._parsed_data)
        return ' '.join([str(i) for i in matches])

# def subs_soln_re(s: str, substr: str) -> list[int]:
#     return [i.start()+1 for i in re.finditer(f"(?={substr})", s)]

# def naiveSearch(txt: str, pat: str) -> list[int]:
#     # O(n*m)
#     matches = []
#     for i in range(len(txt)-len(pat)+1):
#         j = 0
#         while j < len(pat) and txt[i+j] == pat[j]:
#             j += 1
#         if j == len(pat):
#             matches.append(i)
#     return matches

# def find_dna_motif_naive_1(filename: str) -> list[int]:
#   with open(filename) as f:
#     s = f.readline().rstrip()
#     m = f.readline().rstrip()
#   return [i+1 for i in naiveSearch(s, m)]


if __name__ == '__main__':
    SUBSSolution()
