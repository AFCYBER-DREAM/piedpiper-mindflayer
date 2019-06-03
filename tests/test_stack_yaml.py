import os


def test_stack_functions(stack_data):
    errMsg = 'Error: \'stack.yml\' file does not contain any functions.'
    assert 'functions' in stack_data, errMsg


def test_git_ignore(stack_dir):
    path = os.path.join(stack_dir, '.gitignore')
    errMsg = f'Error: No \'.gitignore\' file found in {stack_dir}.'
    assert os.path.exists(os.path.realpath(path)), errMsg


def test_stack_handlers(stack_function, stack_dir):
    path = os.path.join(stack_dir, stack_function['handler'])
    errMsg = f'Error: No directory for {stack_function["handler"]}.'
    assert os.path.exists(os.path.realpath(path)), errMsg


def test_stack_handlers_file(stack_function, stack_dir):
    path = os.path.join(stack_dir, stack_function['handler'], 'handler.py')
    errMsg = (f'Error: \'{stack_function["handler"]}\' does not contain '
              '\'handler.py\' file.')
    assert os.path.exists(os.path.realpath(path)), errMsg


def test_stack_handlers_requires(stack_function, stack_dir):
    path = os.path.join(stack_dir, stack_function['handler'],
                        'requirements.txt')
    errMsg = (f'Error: \'{stack_function["handler"]}\' does not contain '
              '\'requirements.txt\' file.')
    assert os.path.exists(os.path.realpath(path)), errMsg


def test_stack_handlers_init(stack_function, stack_dir):
    path = os.path.join(stack_dir, stack_function['handler'],
                        '__init__.py')
    errMsg = (f'Error: \'{stack_function["handler"]}\' does not contain '
              '\'__init__.py\' file.')
    assert os.path.exists(os.path.realpath(path)), errMsg


def test_stack_langs(stack_function, stack_dir):
    path = os.path.join(stack_dir, 'template', stack_function['lang'])
    errMsg = (f'Error: No directory for {stack_function["lang"]} is present in '
              '\'template\' directory.')
    assert os.path.exists(os.path.realpath(path)), errMsg


def test_stack_langs_dockerfile(stack_function, stack_dir):
    path = os.path.join(stack_dir, 'template', stack_function['lang'],
                        'Dockerfile')
    errMsg = (f'Error: \'template/{stack_function["lang"]}/\' does not contain '
              '\'Dockerfile\'.')
    assert os.path.exists(os.path.realpath(path)), errMsg


def test_stack_langs_requires(stack_function, stack_dir):
    path = os.path.join(stack_dir, 'template', stack_function['lang'],
                        'requirements.txt')
    errMsg = (f'Error: \'template/{stack_function["lang"]}/\' does not contain '
              '\'requirements.txt\' file.')
    assert os.path.exists(os.path.realpath(path)), errMsg


def test_only_langs(stack_data, stack_dir):
    lang_set = {v['lang'] for k, v in stack_data['functions'].items()}
    dir_set = set(os.listdir(os.path.join(stack_dir, 'template')))
    warnMsg = ('Warning: Unused language templates are present in \'template\' '
               'directory.')

    assert len(dir_set - lang_set) == 0, warnMsg
