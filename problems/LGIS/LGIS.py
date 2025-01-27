"""Longest Increasing Subsequence"""

from shared.solution import Solution


class LGISSolution(Solution):

    @staticmethod
    def algorithm(seq: list[int], increasing: bool = True) -> tuple[int, ...]:
        """
        Returns the longest increasing (default) or decreasing subsequence.

        Args:
            seq (List[int]): List of integers.
            increasing (bool, optional): If False, returns a descending subsequence. Defaults to True.

        Returns:
            Tuple[int, ...]: Longest increasing subsequence.
        """
        dp = [1] * len(seq)      # dp array
        parent = [-1] * len(seq)  # to reconstruct the subsequence

        for i in range(1, len(seq)):
            for j in range(i):
                check = seq[i] > seq[j] if increasing else seq[i] < seq[j]
                if check and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j

        max_idx = dp.index(max(dp))
        longest_subseq = []
        while max_idx != -1:
            longest_subseq.append(seq[max_idx])
            max_idx = parent[max_idx]

        return tuple(longest_subseq[::-1])

    def _parse(self) -> list[int]:
        with open(self._input_file) as f:
            next(f)
            s = next(f)
        return [int(i) for i in s.split()]

    def _solve(self) -> str:
        longest_incr_subseq = ' '.join(
            map(str, self.algorithm(self._parsed_data))
        )
        longest_decr_subseq = ' '.join(
            map(str, self.algorithm(self._parsed_data, increasing=False))
        )
        return f"{longest_incr_subseq}\n{longest_decr_subseq}"


if __name__ == '__main__':
    LGISSolution()
