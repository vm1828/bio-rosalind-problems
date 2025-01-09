import os
import pytest
from tempfile import TemporaryDirectory

from shared.solution import Solution


def solution_output(cls: Solution, test_input: str) -> str:
    """Creates tmp file with test input and uses it to evaluate the solution.

    Args:
        cls (Type[Solution]): The class being tested, which implements the solution logic.
        test_input (str): Input data to be tested.

    Returns:
        actual_output (str): Actual test output
    """
    with TemporaryDirectory() as tmp_dir:
        tmp_input_file = os.path.join(tmp_dir, "tmp_problem.txt")
        tmp_output_file = os.path.join(tmp_dir, "tmp_output.txt")

        # write test input into a file
        with open(tmp_input_file, 'w') as f:
            f.write(test_input)

        # run code
        cls(tmp_input_file, tmp_output_file)

        # read output
        with open(tmp_output_file) as f:
            actual_output = f.read()

    return actual_output


@pytest.fixture
def compare_in_any_order():
    """Compares actual and expected outputs, ignoring order."""
    def _compare(solution_output: str, expected_output: str) -> bool:
        return set(solution_output.split()) == set(expected_output.split())
    return _compare


# def run_with_tmp_file(func: Callable, s: str) -> Any:
#     """
#     Creates tmp file with test input and passes it to the tested function.

#     Args:
#         func (Callable): Function to test.
#         s (str): Test input to write to the file.
#     """

#     with TemporaryDirectory() as tmp_dir:
#         tmp_file = os.path.join(tmp_dir, "tmp.txt")
#         with open(tmp_file, 'w') as f:
#             f.write(s)
#         result = func(tmp_file)

#     return result


# def _timeit(n=1):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             total = 0
#             for _ in range(n):
#                 start = time.perf_counter()
#                 result = func(*args, **kwargs)
#                 end = time.perf_counter()
#                 total += (end - start)
#             avg_time = round(total/n, 6)
#             print(
#                 f"Average execution time of *{args[0].__name__}* over {n} calls: {avg_time} seconds") if avg_time else None
#             return result
#         return wrapper
#     return decorator


# @_timeit(n=100)
# def assess_performance(func: Callable, test_file: str) -> None:
#     """_summary_

#     Args:
#         func (Callable): function to test
#         test_file (str): file with test input
#     """
#     func(test_file)
