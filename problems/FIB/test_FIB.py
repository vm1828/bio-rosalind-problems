from problems.FIB.FIB import FIBSolution
from shared.testing_utils import solution_output

test_input = "5 3"
expected_output = "19"


def test_FIBSolution():
    assert solution_output(FIBSolution, test_input) == expected_output
