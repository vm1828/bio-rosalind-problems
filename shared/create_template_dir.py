# script for creating template directories for problems

import os
import sys


def create_template_dir(id, title=False):
    """Create problem dir template"""

    if os.path.exists(id):
        print(f"Directory '{id}' already exists.")
        return

    # Create dir
    os.makedirs(id)

    # Create files
    init_file = os.path.join(id, '__init__.py')
    main_file = os.path.join(id, f'{id}.py')
    test_file = os.path.join(id, f'test_{id}.py')
    for file_path in [init_file, main_file, test_file]:
        open(file_path, 'a').close()

    # Write title to the main file
    if title:
        with open(main_file, 'w') as f:
            f.write(f'# {title}')

    print(
        f"Template directory'{id}' with files '__init__.py', '{id}.py', and 'test_{id}.py' created.")


# if __name__ == "__main__":
#     # create single dir using cli
#     if len(sys.argv) != 2:
#         print("Usage: python3 ./shared/create_template_dir.py <id>")
#         sys.exit(1)

#     id = sys.argv[1]
#     create_template_dir(id)

# if __name__ == "__main__":
#     # batch create problem template directories
#     problems = """FIB Rabbits and Recurrence Relations
#     GC Computing GC Content
#     HAMM Counting Point Mutations
#     IPRB Mendel's First Law"""

#     # Parse the data into tuples
#     problems = [
#         tuple(line.split(maxsplit=1)) for line in problems.strip().split("\n")
#     ]

#     # Print the result
#     for problem in problems:
#         create_template_dir(*problem)
