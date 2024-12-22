from problems.FIBD.FIBD import FIBDSolution
from shared.testing_utils import solution_output


test_input = "6 3"
expected_output = "4"


def test_FIBDSolution():
    assert solution_output(FIBDSolution, test_input) == expected_output
