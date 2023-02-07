"""
This module contains the configuration and fixtures for the project
services.

Session and test running activities will invoke all hooks defined in
conftest.py files closer to the root of the filesystem.
"""
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
from pathlib import Path
from typing import Final

import pytest

from evoml_python_commons import conf_mgr

from tests import TESTS_PATH

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                           Update environment configuration                                           #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

TESTS_ENV_FILE_PATH: Final[Path] = TESTS_PATH.joinpath(".env.test.integration")


@pytest.fixture(scope="package", autouse=True)
def set_env_configuration():
    """Update the environment configuration for this package"""
    conf_mgr.update_conf_mgr(env_file=str(TESTS_ENV_FILE_PATH))


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                          Global testing constants and Types                                          #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                     Fixtures accessible by all integration tests                                     #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
