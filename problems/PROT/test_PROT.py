from problems.PROT.PROT import prot_soln

test_input = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
test_output = "MAMAPRTEINSTRING"


def test_prot_soln():
    assert prot_soln(test_input) == test_output
