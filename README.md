# evoml-python-commons

Evoml common feature set in python language

### Prerequisites

- python 3.8

## Table of Contents

* [Authors](AUTHORS.md)
* [Changelog](CHANGELOG.md)
* [Useful scripts](docs/useful_scripts.md)
* [Set up a Python environment](docs/conda_basics.md)
* [Basic development steps](docs/development.md)

## Setup pre-commit

### Install pre-commit package

```shell
user@pc:~/evoml-python-commons$ conda activate env-py38
(env-py38) user@pc:~/evoml-python-commons$ pip install pre-commit
```

### Setup pre-commit and pre-push hooks, just after repository clone

```shell
(env-py38) user@pc:~/evoml-python-commons$ pre-commit install \
    -t pre-commit pre-commit install \
    -t pre-push pre-commit install \
    --hook-type commit-msg
```

## Information for Users

### Important source files

- [\_\_init\_\_.py](src/evoml_python_commons_rest/__init__.py): Expose the most important modules of the library.
- [py.typed](src/evoml_python_commons_rest/py.typed): File to create PEP 561 compatible packages. To publish a
  library package to a package repository yourself (e.g. on PyPI) for either internal or external use in type checking,
  packages that supply type information via type comments or annotations in the code should put a `py.typed` file in
  their package directory.

### Package

- **Default**: The default packaging of this library is **`BUILDTOOL=wheel`**.

```shell
(env-py38-evoml-python-commons) user@pc:~/evoml-python-commons$ make package
```

- **Open source**:

```shell
(env-py38-evoml-python-commons) user@pc:~/evoml-python-commons$ make package BUILDTOOL=wheel
```

- **Binary distribution**:

```shell
(env-py38-evoml-python-commons) user@pc:~/evoml-python-commons$ make package BUILDTOOL=nuitka
```

### Usage

Installation:

```shell
(env-py38-evoml-python-commons) user@pc:~/evoml-python-commons$ pip install evoml-python-commons
```

### Configuration

The values indicated as an example in each of the variables is the value that will be taken by default if you do not
specify that variable in the file '.env'

#### Logging configuration

For more details, see [loguru](https://loguru.readthedocs.io/en/stable/api/logger.html)

| Variable              | Description                                                                                                                                                                 | Default value             |
| --------------------- |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| ------------------------- |
| LOGGER_ENABLE         | Flag that indicates whether the logging configuration should be initialized (true) or, if on the contrary, this configuration is already supposed to be initialized (false) | false |
| LOGGER_SINK           | Path to the log file.                                                                                                                                                       | /tmp/evoml-python-commons/logs/evoml_python_commons.log |
| LOGGER_LEVEL          | The minimum severity level from which logged messages should be sent to the sink. <br> - Options: `critical, error, warning, success, info, debug, trace`                   | INFO |
| LOGGER_ROTATION       | A condition indicating whenever the current logged file should be closed and a new one started.                                                                             | "12:00"  # New file is created each day at noon |
| LOGGER_RETENTION      | A directive filtering old files that should be removed during rotation or end of program.                                                                                   | "1 month" |

