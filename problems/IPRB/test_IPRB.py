from problems.IPRB.IPRB import IPRBSolution
from shared.testing_utils import solution_output

test_input = "2 2 2"
expected_output = "0.78333"


def test_IPRBSolution():
    assert solution_output(IPRBSolution, test_input) == expected_output
