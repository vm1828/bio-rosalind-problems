"""Mortal Fibonacci Rabbits"""

from shared.solution import Solution


class FIBDSolution(Solution):

    @staticmethod
    def algorithm(n: int, m: int) -> int:
        """Simulates the growth of a rabbit population with aging and mortality constraints.

        Args:
            months (int): The total number of months.
            m (int): The lifespan of a rabbit in months.

        Returns:
            int: The total number of rabbit pairs alive at the end of month n.
        """
        newborn, mature = 1, 0  # Initial state: 1 newborn pair, 0 mature pairs
        queue = [1]  # Track newborns
        for _ in range(2, n+1):
            new_newborn = mature  # Newborns are current mature rabbits
            dead = queue.pop(0) if len(queue) >= m else 0  # Died this month
            mature = mature + newborn - dead  # Update mature
            queue.append(new_newborn)  # Track newborns
            newborn = new_newborn
        return newborn + mature

    def _parse(self) -> tuple[int]:
        with open(self._input_file) as f:
            n, m = f.readline().strip().split(' ')
        return int(n), int(m)

    def _solve(self) -> str:
        return str(self.algorithm(*self._parsed_data))


# def fibd(n, m):
#     seq = [(1, 0), (0, 1)]    # (newborn, mature)
#     for i in range(2, n):
#         newborn = seq[i-1][1]
#         dead = seq[i-m][0] if len(seq) >= m else 0
#         mature = sum(seq[i-1]) - dead
#         seq.append((newborn, mature))
#         print(f'Month {i+1}: {sum(seq[i])} pairs')
#     return sum(seq[-1])


if __name__ == '__main__':
    FIBDSolution()
