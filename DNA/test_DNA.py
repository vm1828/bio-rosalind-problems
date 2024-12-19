from DNA.DNA import count_dna_nucleobases

test_input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
test_output = (20, 12, 17, 21)


def test_count_dna_nucleobases():
    assert count_dna_nucleobases(test_input) == test_output
