from problems.PROT.PROT import PROTSolution
from shared.testing_utils import solution_output


test_input = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
expected_output = "MAMAPRTEINSTRING"


def test_PROTSolution():
    assert solution_output(PROTSolution, test_input) == expected_output
