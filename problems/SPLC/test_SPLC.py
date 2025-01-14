from problems.SPLC.SPLC import SPLCSolution
from shared.testing_utils import solution_output


test_input = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT"""
expected_output = "MVYIADKQHVASREAYGHMFKVCA\n"


def test_SPLCSolution():
    assert solution_output(SPLCSolution, test_input) == expected_output
