from problems.MPRT.MPRT import MPRTSolution
from shared.testing_utils import solution_output


test_input = """A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST"""
expected_output = """B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614\n"""


def test_MPRTSolution():
    assert solution_output(MPRTSolution, test_input) == expected_output
