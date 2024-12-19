import os
import sys


def create_template_dir(problem_name):
    """Create problem dir template"""
    os.makedirs(problem_name)

    init_file = os.path.join(problem_name, '__init__.py')
    main_file = os.path.join(problem_name, f'{problem_name}.py')
    test_file = os.path.join(problem_name, f'test_{problem_name}.py')

    # Create files
    for file_path in [init_file, main_file, test_file]:
        open(file_path, 'a').close()

    print(
        f"Template directory'{problem_name}' with files '__init__.py', '{problem_name}.py', and 'test_{problem_name}.py' created.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 create_template_dir.py <problem_name>")
        sys.exit(1)

    problem_name = sys.argv[1]
    create_template_dir(problem_name)
