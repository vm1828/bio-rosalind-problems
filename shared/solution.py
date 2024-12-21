"""Rosalind solution module"""

import os
from tempfile import TemporaryDirectory
from abc import ABC, abstractmethod
from typing import Any

from shared.constants import PROBLEM, SOLUTION


class Solution(ABC):
    """A class that processes input data, applies a solution algorithm, 
    and writes the result to an output file.
    """

    def __init__(self, input_file: str = PROBLEM, output_file: str = SOLUTION):
        """
        Args:
            input_file (str): Path to the input file containing the data for processing.
            output_file (str): Path to the output file where the solution will be written.

        Attributes:
            _input_file (str): Path to the input file.
            __output_file (str): Path to the output file.
            _parsed_data (Any): The data parsed from the input file, prepared for use in the solution algorithm.
            solution (str): The formatted solution as a string, generated by applying the solution algorithm.
        """
        self._input_file = input_file
        self.__output_file = output_file

        self._parsed_data: Any = self._parse()
        self._solution: str = self._solve()
        self.__write_solution_to_file()

    def _parse(self) -> str:
        """Parses the input file and returns the extracted data for processing."""
        with open(self._input_file) as f:
            self._parsed_data = f.read().strip()
        return self._parsed_data

    def _solve(self) -> str:
        """Applies the solution algorithm to the parsed data and returns the formatted result as a string."""
        return self.algorithm(self._parsed_data)

    def __write_solution_to_file(self):
        with open(self.__output_file, 'w') as f:
            f.write(self._solution)

    @staticmethod
    @abstractmethod
    def algorithm() -> Any:
        """Abstract static method to be implemented by subclasses and reusable upon import."""
        pass

    @classmethod
    def test_solution(cls, test_input, expected_output) -> bool:
        """Creates tmp file with test input and uses it to test the solution.

        Args:
            test_input (str): Test input
            test_input (str): Test output

        Returns:
            result (bool): Testing result (True of False)
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

        return actual_output == expected_output
