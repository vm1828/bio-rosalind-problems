"""Enumerating Gene Orders"""

from shared.solution import Solution


class PERMSolution(Solution):

    @staticmethod
    def algorithm(lst: list) -> list[list]:
        """
        Recursively generates all permutations of the input list.

        Args:
            lst (list): A list of elements to permute.

        Returns:
            list[list]: A list of all permutations, where each permutation is a list of elements.
        """
        # return list(itertools.permutations(lst))
        if len(lst) <= 1:
            return [lst]
        return [
            m[:i] + [lst[0]] + m[i:]
            for m in PERMSolution.algorithm(lst[1:])
            for i in range(len(m) + 1)
        ]

    def _parse(self) -> list[int]:
        with open(self._input_file) as f:
            n = int(f.readline().strip())
        return list(range(1, n+1))

    def _solve(self) -> str:
        permutations = self.algorithm(self._parsed_data)
        formatted_result = f"{len(permutations)}\n" + \
            "\n".join(" ".join(list(map(str, p))) for p in permutations) + "\n"
        print(formatted_result)
        return formatted_result


if __name__ == '__main__':
    PERMSolution()
