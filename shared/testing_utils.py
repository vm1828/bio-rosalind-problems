import os
import time

from typing import Callable, Any
from tempfile import TemporaryDirectory


def run_with_tmp_file(func: Callable, s: str) -> Any:
    """
    Creates tmp file with test input and passes it to the tested function.

    Args:
        func (Callable): Function to test.
        s (str): Test input to write to the file.
    """

    with TemporaryDirectory() as tmp_dir:
        tmp_file = os.path.join(tmp_dir, "tmp.txt")
        with open(tmp_file, 'w') as f:
            f.write(s)
        result = func(tmp_file)

    return result


def timeit(n=1):
    """Decorator is used for testing function performance over n executions

    Args:
        n (int, optional): Number of executions. Defaults to 1.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            total = 0
            for _ in range(n):
                start = time.perf_counter()
                func(*args, **kwargs)
                end = time.perf_counter()
                total += (end - start)
            avg_time = round(total/n, 6)
            print(
                f"Average execution time of *{args[0].__name__}* over {n} calls: {avg_time} seconds") if avg_time else None
            return func(*args, **kwargs)
        return wrapper
    return decorator


@timeit(n=100)
def test_performance(func: Callable, test_file: str) -> None:
    """_summary_

    Args:
        func (Callable): function to test
        test_file (str): file with test input
    """
    func(test_file)
