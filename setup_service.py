#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
import os
import sys
from pathlib import Path

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                        Utils                                                         #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

root_path = Path(__file__).parent.resolve()
setup_path = root_path.joinpath("setup")


def get_requirements(file_path: Path):
    """Reads package dependencies and returns a list of requirement.
    e.g. ["django==1.5.1", "mezzanine==1.4.6"]
    """
    with file_path.open() as in_file:
        return [str(r) for r in parse_requirements(in_file)]


def get_python_requires():
    _python_requires = "3.8"
    try:
        float(_python_requires)
    except ValueError:
        return _python_requires
    return f">={_python_requires}"


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                     Definitions                                                      #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

setup_package_dir = "src"

__version__ = setup_path.joinpath(".version").read_text()
__project_title__ = "evoml-python-commons-service"
__project_name__ = "evoml-python-commons-service"
__package_name__ = "evoml_python_commons_service"
__description__ = "Evoml common feature set in python language"
__company_name__ = "Turing Intelligence Technology"
__license__ = "MIT License"
__copyright__ = "Copyright 2023 Turing Intelligence Technology"

requirements = get_requirements(file_path=setup_path.joinpath("requirements.txt"))
tests_requirements = get_requirements(file_path=setup_path.joinpath("requirements_develop.txt"))

readme = root_path.joinpath("README.md").read_text()
history = root_path.joinpath("CHANGELOG.md").read_text()

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

if sys.argv[-1] == "info":
    print(f"Project title   : {__project_title__}")
    print(f"Project name    : {__project_name__}")
    print(f"Package name    : {__package_name__}")
    print(f"Description     : {__description__}")
    print(f"Project version : {__version__}")
    print(f"Company name    : {__company_name__}")
    print(f"License         : {__license__}")
    print(f"Copyright       : {__copyright__}")
    sys.exit()

# ───────────────────────────────────────────────────────────────────────────────────────────── #
# ─── Setup
# ───────────────────────────────────────────────────────────────────────────────────────────── #
setup(
    name=__project_name__,
    version=os.environ.get("VERSION", __version__),
    description=__description__,
    long_description=f"{readme}\n\n{history}",
    long_description_content_type="text/markdown",
    author=__company_name__,
    url="https://github.com/turintech/evoml-python-commons.git",

    license=__license__,

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 0.0.0",

        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # "Topic :: Topic 1 :: Topic2",

        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by "pip install". See instead "python_requires" below.
        "Programming Language :: Python :: 3.8",
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a list of additional keywords, separated
    # by commas, to be used to assist searching for the distribution in a
    # larger catalog.
    keywords=__project_title__,  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    # package_dir={"": "metaml"},  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    # packages=find_packages(where="metaml.*"),  # Required
    packages=find_packages(
        find_packages(include=[__package_name__, f"{__package_name__}.*"], where=setup_package_dir)
    ),
    package_dir={
        "": setup_package_dir
    },

    # Add the data files included in the "/src" packages
    package_data={
        # "/src/*"
        # "": ["*.ini", "*.yml", "*.json"]
        "": ["py.typed"]
    },

    scripts=[
    ],

    # Specify which Python versions you support. In contrast to the
    # "Programming Language" classifiers above, "pip install" will check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires=get_python_requires(),

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip"s requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=requirements,  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     "console_scripts": [
    #         "main=main:main",
    #     ],
    # },
)
