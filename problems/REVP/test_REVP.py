from problems.REVP.REVP import REVPSolution
from shared.testing_utils import solution_output


test_input = """>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT"""
expected_output = """4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4\n"""


def test_REVPSolution():
    assert solution_output(REVPSolution, test_input) == expected_output
