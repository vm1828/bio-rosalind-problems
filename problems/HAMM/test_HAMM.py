from problems.HAMM.HAMM import hamm_soln
from shared.testing_utils import run_with_tmp_file

test_input = """GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
"""
test_output = 7


def test_hamm_soln():
    assert run_with_tmp_file(hamm_soln, test_input) == test_output
