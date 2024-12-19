from RNA.RNA import dna_to_rna

test_input = "GATGGAACTTGACTACGTAAATT"
test_output = "GAUGGAACUUGACUACGUAAAUU"


def test_dna_to_rna():
    assert dna_to_rna(test_input) == test_output
