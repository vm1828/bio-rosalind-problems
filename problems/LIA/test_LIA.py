from problems.LIA.LIA import LIASolution
from shared.testing_utils import solution_output


test_input = "2 1"
expected_output = "0.684\n"


def test_LIASolution():
    assert solution_output(LIASolution, test_input) == expected_output
