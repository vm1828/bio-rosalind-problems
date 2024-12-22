from problems.GRPH.GRPH import GRPHSolution
from shared.testing_utils import solution_output


test_input = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG"""
expected_output = """Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""


def test_GRPHSolution():
    assert solution_output(GRPHSolution, test_input) == expected_output
