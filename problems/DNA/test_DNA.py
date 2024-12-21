from problems.DNA.DNA import DNASolution


test_input = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
test_output = "20 12 17 21"


# def test_dna_soln():
#     assert dna_soln(test_input) == test_output

def test_DNASolution():
    assert DNASolution().test_solution(test_input, test_output)
