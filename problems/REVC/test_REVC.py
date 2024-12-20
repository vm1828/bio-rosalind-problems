from problems.REVC.REVC import revc_soln

test_input = "AAAACCCGGT"
test_output = "ACCGGGTTTT"


def test_revc_soln():
    assert revc_soln(test_input) == test_output
