#! /usr/bin/env python3

from sys import argv
from pathlib import Path

import yaml
import os


def validate_file(passed_file):
    user_file = Path(passed_file)

    # See if the argument is a valid path.
    try:
        user_file.resolve(strict=True)
    except FileNotFoundError:
        print(f"Error: {passed_file} could not be found from the current"
              + " directory.")
    else:
        # The passed path is valid, now check if path is a file or directory.
        if user_file.is_file():
            # If the path is a file, start testing.
            test_structure(user_file)
        elif user_file.is_dir():
            # If path is a directory, recommend user tries again.
            print(f"Warning: {passed_file} is a directory, not a file.")
            print("Try again with one of the files within the directory.")
        else:
            # In case path is valid but inaccessible...
            print(f"Error: {passed_file} is inaccessible.")
            print("Please try again.")


def test_structure(yaml_file):
    # Print the "functions" branch(es) to stdout.
    with open(yaml_file, 'r') as f:
        stack_yaml = yaml.safe_load(f)

    # Test for 'functions' key in YAML file.
    assert 'functions' in stack_yaml, "Error: 'functions' not defined in file."

    #parent_dir = os.path.dirname(str(yaml_file))
    project_path = os.path.realpath(os.path.dirname(str(yaml_file)))

    # Test for '.gitignore' file in base directory.
    assert os.path.exists(os.path.join(project_path, '.gitignore'))

    for key, value in stack_yaml['functions'].items():
        # Test for template directory named after lang value.
        assert os.path.exists(os.path.join(project_path, 'template',
                                           value['lang']))

        # Test for 'Dockerfile' in language specific template directory.
        assert os.path.exists(os.path.join(project_path, 'template',
                                           value['lang'], 'Dockerfile'))

        # Test for 'requirements.txt' in function specific directory.
        assert os.path.exists(os.path.join(project_path, key,
                                           'requirements.txt'))

        # Test for 'handler.py' in function specific directory.
        assert os.path.exists(os.path.join(project_path, key, 'handler.py'))

        # Test for '__init__.py' in function specific directory.
        assert os.path.exists(os.path.join(project_path, key, '__init__.py'))


if __name__ == "__main__":
    try:
        script, arg01 = argv
    except ValueError:
        print("Error: Too few arguments provided.")
    else:
        validate_file(arg01)
