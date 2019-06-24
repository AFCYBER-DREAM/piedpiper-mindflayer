# PiperCI Mindflayer
[![Build Status](https://travis-ci.com/AFCYBER-DREAM/piperci-mindflayer.svg?branch=master)](https://travis-ci.com/AFCYBER-DREAM/piperci-mindflayer)

### Table of Contents

* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Inputs and Outputs](#inputs-and-outputs)
* [Running the Tests](#running-the-tests)
* [Travis-CI Integration](#travis-ci-integration)
* [Test Prerequisites](#test-prerequisites)
* [Contributing](#contributing)
* [Versioning](#versioning)
* [Authors](#authors)
* [License](#license)

## Getting Started

Mindflayer is a series of tests that verifies the directory structure of
PiperCI FaaS projects/modules.  At the time of this writing, Mindflayer runs
the following tests:

* Functions are defined in FaaS module's `stack.yml` file.
* FaaS module project has a `.gitignore` file.
* Each function defined in `stack.yml` has a subdirectory matching the name of
  the assigned handler object.
* Each handler object's parent directory contains the following files:
  * `handler.py`
  * `requirements.txt`
  * `__init__.py`
* Each language used by defined functions has a dedicated subdirectory within
  `./template/`.
* Each language subdirectory in `./template/` contains the following files:
  * `Dockerfile`
  * `requirements.txt`
* The `./template/` directory only contains subdirectories that are called from
  the functions defined in `stack.yml`.

### Prerequisites

* pytest
* pyYAML

### Usage

To utilize Mindflayer, enter the parent directory for the PiperCI module and
then call the `test_stack_yaml.py` script within the `tests` directory of the
`piperci-mindflayer` project.  See [Running the Tests](#running-the-tests) for
example of usage.

## Inputs and Outputs

Mindflayer does not expect any direct inputs or arguments in order to run.

Output for Mindflayer is in the pytest format.  The following output is an
example of how a passing test will appear for a project with a single function.

```shell
$ pytest ../piperci-mindflayer/tests/test_stack_yaml.py
============================= test session starts ==============================
platform linux -- Python 3.7.3, pytest-4.5.0, py-1.8.0, pluggy-0.12.0
rootdir: /home/user/Projects
collected 10 items

../piperci-mindflayer/tests/test_stack_yaml.py ..........              [100%]

========================== 10 passed in 0.01 seconds ===========================
```

> **NOTE:**
>
> The number of tests run by Mindflayer is subject to change between projects.
> Mindflayer will run five (5) of the tests once for each function that is
> properly defined in the `stack.yml` file, and three (3) of the tests once for
> each unique language used in the defined function(s).

## Running the Tests

As mentioned in the [Usage](#usage) section above, Mindflayer is called from the
root directory of a PiperCI module.

```shell
$ cd piperci-example_module-faas
# Verify that the project directory has a `stack.yml` file.
$ ls | grep stack.yml
stack.yml
# Run the pytest module against the project.
$ pytest ../piperci-mindflayer/tests/test_stack_yaml.py
```

### Travis-CI Integration

To add Mindflayer to a Travis-CI pipeline, it is recommended to utilize Tox.
The section of the `tox.ini` file that runs the Mindflayer tests should have at
least what is outlined in the example below:

```data
[testenv:sanity]
deps =
    pluggy==0.12.0
    pytest==4.5.0
    PyYAML==5.1
commands_pre =
    wget https://github.com/AFCYBER-DREAM/piperci-mindflayer/archive/v1.0.0.zip \
        -O /tmp/piperci-mindflayer.zip
    unzip /tmp/piperci-mindflayer.zip -d /tmp/
commands =
    pytest /tmp/piperci-mindflayer-1.0.0/tests/test_stack_yaml.py
```

> **NOTE:**
>
> It is user preference to determine where Mindflayer will be downloaded and run
> from.  The order in which a pipeline runs is also subjective, but the
> development team recommends running the Mindflayer tests just after all syntax
> scripts, but before any unit- or functional-testing.  Change the `.travis.yml`
> file accordingly.

### Test Prerequisites

As outlined in the [Prerequisites](#prerequisites) section, Mindflayer requires
that both `pytest` and `pyYAML` are installed and accessible to the running
environment.  Install both of these python modules with the following command:

```shell
$ pip install --user pytest PyYAML
```

To begin getting more useful output from Mindflayer, ensure that the PiperCI
module has a `stack.yml` file in it's root directory.  The `stack.yml` file
should be structured like the following example:

```yaml
---
provider:
  name: faas
  gateway: http://127.0.0.1:8080
functions:
  piedpier-example_module-function:
    lang: python
    handler: ./piperci-example_module-function
    image: piperci-example_module-function:latest
```

If a `stack.yml` file exists within the module's root directory and structured
similarly to the above, the pytest output will provide errors showing what
files and directories need to be present for the module to meet the standard
file structure.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/AFCYBER-DREAM/piperci-picli)
for details on our code of conduct, and the process for submitting pull requests
to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the
[tags on this repository](https://github.com/piperci-mindflayer/tags).

## Authors

See also the list of
[contributors](https://github.com/AFCYBER-DREAM/piperci-mindflayer/contributors)
 who participated in this project.

## License

MIT
