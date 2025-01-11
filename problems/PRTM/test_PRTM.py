from problems.PRTM.PRTM import PRTMSolution
from shared.testing_utils import solution_output


test_input = "SKADYEK"
expected_output = "821.392\n"


def test_PRTMSolution():
    assert solution_output(PRTMSolution, test_input) == expected_output
