"""Counting Point Mutations"""

from shared.constants import PROBLEM, SOLUTION


def hamm_soln(filename: str) -> int:
    with open(filename) as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
        assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# def hamm_soln(filename: str) -> int:
#   with open(filename) as f:
#     s1 = f.readline().strip()
#     s2 = f.readline().strip()
#     assert len(s1) == len(s2)
#   count = 0
#   for i in range(len(s1)):
#     if s1[i] != s2[i]:
#       count += 1
#   return count


if __name__ == '__main__':
    solution = str(hamm_soln(PROBLEM))
    with open(SOLUTION, 'w') as f:
        f.write(solution)
