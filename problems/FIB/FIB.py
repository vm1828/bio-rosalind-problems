"""Rabbits and Recurrence Relations"""

from shared.constants import PROBLEM, SOLUTION


def fib_soln(n: int, k: int = 1) -> int:
    """Compute the nth Fibonacci number.

    Args:
        n (int): Number of days
        k (int, optional): Reproduction factor (offsprings multiplier). Defaults to 1.

    Returns:
        int: nth Fibonacci number
    """
    a = 1
    b = 1
    print(f'Month 1: {a} pair')
    print(f'Month 2: {b} pair')
    for i in range(3, n+1):
        a, b = b, a*k+b
        print(f'Month {i}: {b} pairs')
    return b


if __name__ == '__main__':
    with open(PROBLEM) as f:
        n, k = f.readline().strip().split(' ')
        n, k = int(n), int(k)
    solution = str(fib_soln(n, k))
    with open(SOLUTION, 'w') as f:
        f.write(solution)
