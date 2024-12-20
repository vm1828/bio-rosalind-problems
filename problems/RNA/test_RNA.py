from problems.RNA.RNA import rna_soln

test_input = "GATGGAACTTGACTACGTAAATT"
test_output = "GAUGGAACUUGACUACGUAAAUU"


def test_rna_soln():
    assert rna_soln(test_input) == test_output
