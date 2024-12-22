"""Rabbits and Recurrence Relations"""

from shared.solution import Solution


class FIBSolution(Solution):

    @staticmethod
    def algorithm(n: int, k: int = 1) -> int:
        """Compute the nth Fibonacci number.

        Args:
            n (int): Number of days.
            k (int, optional): Reproduction factor (offsprings multiplier). Defaults to 1.

        Returns:
            int: nth Fibonacci number.
        """
        a = 1
        b = 1
        print(f'Month 1: {a} pair')
        print(f'Month 2: {b} pair')
        for i in range(3, n+1):
            a, b = b, a*k+b
            print(f'Month {i}: {b} pairs')
        return b

    def _parse(self) -> tuple[int]:
        with open(self._input_file) as f:
            n, k = f.readline().strip().split(' ')
            n, k = int(n), int(k)
        return n, k

    def _solve(self) -> str:
        return str(self.algorithm(*self._parsed_data))


if __name__ == '__main__':
    FIBSolution()
