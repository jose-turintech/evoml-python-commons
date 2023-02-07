"""
The goal of this module is to implement the tests of the base_data_types module
"""
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
import pytest

from evoml_python_commons.conf.conf_manager import conf_mgr
from evoml_python_commons.conf.logger_conf import FileLoggerConf

from tests.tests_base.base_test_conf_mgr import BaseTestConfManager
from tests.tests_integration.conftest import TESTS_ENV_FILE_PATH


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                      Test Class                                                      #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


class TestConfManager(BaseTestConfManager):
    """Tests class of ConfManager"""

    env_file = TESTS_ENV_FILE_PATH
    expected_init_logging_conf = FileLoggerConf(
        enable=True,
        level="debug",
        sink="/tmp/evoml-python-commons/tests/logs/evoml_python_commons_integration.log",
    )

    # --------------------------------------------------------------------------------------------------

    def test_conf_mgr(self):
        """This method validates the conf_mgr's status"""
        self.case.assertEqual(str(self.env_file), conf_mgr.env_file)
        self.assert_dict(expected=self.expected_init_logging_conf, result=conf_mgr.logging_conf, msg="logging_conf")


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

if __name__ == "__main__":
    pytest.main()
