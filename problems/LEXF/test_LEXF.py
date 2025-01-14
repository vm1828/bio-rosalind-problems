from problems.LEXF.LEXF import LEXFSolution
from shared.testing_utils import solution_output


test_input = """A C G T
2"""
expected_output = """AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT\n"""


def test_LEXFSolution():
    assert solution_output(LEXFSolution, test_input) == expected_output
