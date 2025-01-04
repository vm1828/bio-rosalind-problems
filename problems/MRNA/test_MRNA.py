from problems.MRNA.MRNA import MRNASolution
from shared.testing_utils import solution_output


test_input = "MA"
expected_output = "12\n"


def test_MRNASolution():
    assert solution_output(MRNASolution, test_input) == expected_output
