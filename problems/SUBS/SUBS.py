"""Finding a Motif in DNA"""

import re
from shared.constants import PROBLEM, SOLUTION


def subs_soln(s: str, m: str) -> list[int]:
    matches = []
    i = s.find(m)
    while i != -1:
        matches.append(i+1)
        i = s.find(m, i+1)
    return matches


def subs_soln_re(s: str, m: str) -> list[int]:
    return [i.start()+1 for i in re.finditer(f"(?={m})", s)]


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

# def find_dna_motif_naive_2(filename: str) -> list[int]:
#   with open(filename) as f:
#     s = f.readline().rstrip()
#     m = f.readline().rstrip()
#   matches = []
#   for i in range(len(s)):
#     if s[i:].startswith(m):
#       matches.append(i+1)
#   return matches
#


if __name__ == '__main__':
    with open(PROBLEM) as f:
        s = f.readline().rstrip()
        m = f.readline().rstrip()
    solution = subs_soln(s, m)
    with open(SOLUTION, 'w') as f:
        f.write(solution)
