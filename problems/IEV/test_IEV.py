from problems.IEV.IEV import IEVSolution
from shared.testing_utils import solution_output


test_input = "1 0 0 1 0 1"
expected_output = "3.5\n"


def test_IEVSolution():
    assert solution_output(IEVSolution, test_input) == expected_output
