from problems.LGIS.LGIS import LGISSolution
from shared.testing_utils import solution_output


test_input = """5
5 1 4 2 3"""
expected_output = """1 2 3
5 4 2\n"""


def test_LGISSolution():
    assert solution_output(LGISSolution, test_input) == expected_output
