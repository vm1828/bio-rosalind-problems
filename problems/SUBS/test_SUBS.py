from problems.SUBS.SUBS import SUBSSolution
from shared.testing_utils import solution_output


test_input = """GATATATGCATATACTT
ATAT"""
expected_output = "2 4 10\n"


def test_SUBSSolution():
    assert solution_output(SUBSSolution, test_input) == expected_output
