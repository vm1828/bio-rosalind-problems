from REVC.REVC import reverse_complement

test_input = "AAAACCCGGT"
test_output = "ACCGGGTTTT"


def test_reverse_complement():
    assert reverse_complement(test_input) == test_output
