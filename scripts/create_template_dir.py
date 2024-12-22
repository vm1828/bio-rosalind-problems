# script for creating template directories for problems

import os
# import sys

from problems import PROBLEMS


def create_template_dir(id, title=False):
    """Create problem dir template"""
    directory = os.path.join('problems', id)

    if os.path.exists(directory):
        print(f"Directory '{directory}' already exists.")
        return

    # Create dir
    os.makedirs(directory)

    # Create files
    init_file = os.path.join(directory, '__init__.py')
    main_file = os.path.join(directory, f'{id}.py')
    test_file = os.path.join(directory, f'test_{id}.py')
    for file_path in [init_file, main_file, test_file]:
        open(file_path, 'a').close()

    # Write templates
    class_name = f'{id}Solution'
    MAIN_CODE = f"""\"""{title}\"""

from shared.solution import Solution


class {class_name}(Solution):

    @staticmethod
    def algorithm(s: str):
        \"""...

        Args:
            s (str): ...

        Returns:
            ...: ...
        \"""
        ...


if __name__ == '__main__':
    {class_name}()

"""

    TEST_CODE = f"""from problems.{id}.{id} import {class_name}
from shared.testing_utils import solution_output


test_input = ""
expected_output = ""


# def test_{class_name}():
#     assert solution_output({class_name}, test_input) == expected_output

"""
    if title:
        with open(main_file, 'w') as f:
            f.write(MAIN_CODE)
        with open(test_file, 'w') as f:
            f.write(TEST_CODE)

    print(
        f"Template directory'{directory}' with files '__init__.py', '{id}.py', and 'test_{id}.py' created.")


if __name__ == "__main__":
    # batch create problem template directories

    # Parse the data into tuples
    problems = [
        tuple(line.split(maxsplit=1)) for line in PROBLEMS.strip().split("\n")
    ]

    # Print the result
    for problem in problems[:10]:
        create_template_dir(*problem)

# if __name__ == "__main__":
#     # create single dir using cli
#     if len(sys.argv) != 2:
#         print("Usage: python3 ./shared/create_template_dir.py <id>")
#         sys.exit(1)

#     id = sys.argv[1]
#     create_template_dir(id)
