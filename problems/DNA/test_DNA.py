from problems.DNA.DNA import dna_soln

test_input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
test_output = (20, 12, 17, 21)


def test_dna_soln():
    assert dna_soln(test_input) == test_output
