import os
import yaml

import pytest

_real_stack_path = os.path.realpath('./stack.yml')
with open(_real_stack_path, 'r') as stack_yaml:
    _stack_data = yaml.safe_load(stack_yaml)


@pytest.fixture(scope='session')
def stack_dir():
    return os.path.dirname(_real_stack_path)


@pytest.fixture(scope='session')
def stack_data():
    return _stack_data


def pytest_generate_tests(metafunc):
    if 'stack_function' in metafunc.fixturenames:
        data = []
        for function, values in _stack_data['functions'].items():
            values.setdefault('function', function)
            data.append(values)

        metafunc.parametrize('stack_function',
                             data)
