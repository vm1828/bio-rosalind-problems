from problems.PERM.PERM import PERMSolution
from shared.testing_utils import solution_output, compare_in_any_order


test_input = "3"
expected_output = """6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1\n"""


def test_PERMSolution(compare_in_any_order):
    actual_output = solution_output(PERMSolution, test_input)
    assert compare_in_any_order(actual_output, expected_output, '\n')
