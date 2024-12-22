from problems.HAMM.HAMM import HAMMSolution
from shared.testing_utils import solution_output

test_input = """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
"""
expected_output = "7"


def test_HAMMSolution():
    assert solution_output(HAMMSolution, test_input) == expected_output
