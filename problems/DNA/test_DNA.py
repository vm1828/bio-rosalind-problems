from problems.DNA.DNA import DNASolution
from shared.testing_utils import solution_output


test_input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
expected_output = "20 12 17 21"


def test_DNASolution():
    assert solution_output(DNASolution, test_input) == expected_output
