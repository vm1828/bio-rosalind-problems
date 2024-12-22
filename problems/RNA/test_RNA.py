from problems.RNA.RNA import RNASolution
from shared.testing_utils import solution_output


test_input = "GATGGAACTTGACTACGTAAATT"
expected_output = "GAUGGAACUUGACUACGUAAAUU"


def test_RNASolution():
    assert solution_output(RNASolution, test_input) == expected_output
