from problems.FIB.FIB import fib_soln

test_input = (5, 3)
test_output = 19


def test_fib_soln():
    assert fib_soln(*test_input) == test_output
