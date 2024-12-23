from problems.REVC.REVC import REVCSolution
from shared.testing_utils import solution_output


test_input = "AAAACCCGGT"
expected_output = "ACCGGGTTTT\n"


def test_REVCSolution():
    assert solution_output(REVCSolution, test_input) == expected_output
