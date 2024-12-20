from problems.IPRB.IPRB import iprb_soln
from shared.testing_utils import run_with_tmp_file

test_input = '2 2 2'
test_output = 0.78333


def test_iprb_soln():
    assert run_with_tmp_file(iprb_soln, test_input) == test_output
