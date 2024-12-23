from problems.LCSM.LCSM import LCSMSolution
from shared.testing_utils import solution_output


test_input = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""
expected_output = "TA\n"


def test_LCSMSolution():
    assert solution_output(LCSMSolution, test_input) == expected_output


def test_LCSMSolution_algorithm():
    assert LCSMSolution.algorithm(['GATTACA', 'TAGACCA', 'ATACA']) == 'TA'
