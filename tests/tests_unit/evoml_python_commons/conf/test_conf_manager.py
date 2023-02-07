"""
The goal of this module is to implement the tests of the base_data_types module
"""
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
import pytest

from evoml_python_commons.conf.conf_manager import conf_mgr, ConfManager
from evoml_python_commons.conf.logger_conf import FileLoggerConf

from tests.tests_base.base_test import BaseTest
from tests.tests_unit.conftest import TESTS_ENV_FILE_PATH


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                      Test Class                                                      #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


class TestConfManager(BaseTest):
    """Tests class of ConfManager"""

    env_file = TESTS_ENV_FILE_PATH
    expected_init_logging_conf = FileLoggerConf(
        enable=True,
        level="debug",
        sink="/tmp/evoml-python-commons/tests/logs/evoml_python_commons_unit.log",
    )

    # --------------------------------------------------------------------------------------------------

    def test_conf_mgr(self):
        """This method validates the conf_mgr's status"""

        self.case.assertTrue(conf_mgr.path_conf.is_dir(), "conf_mgr.path_conf.is_dir")
        self.case.assertEqual("conf", conf_mgr.path_conf.name, "conf_mgr.path_conf.name")

        self.case.assertTrue(conf_mgr.path_app.is_dir(), "conf_mgr.path_app.is_dir")
        self.case.assertEqual("evoml_python_commons", conf_mgr.path_app.name, "conf_mgr.path_app.name")

        self.case.assertTrue(conf_mgr.path_src.is_dir(), "conf_mgr.path_src.is_dir")
        self.case.assertEqual("src", conf_mgr.path_src.name, "conf_mgr.path_src.name")

        self.case.assertTrue(conf_mgr.path_root.is_dir(), "conf_mgr.path_root.is_dir")
        self.case.assertEqual("evoml-python-commons", conf_mgr.path_root.name, "conf_mgr.path_root.name")

        self.case.assertEqual(str(self.env_file), conf_mgr.env_file)
        self.assert_dict(expected=self.expected_init_logging_conf, result=conf_mgr.logging_conf, msg="logging_conf")

    def test_conf_mgr_init_none(self):
        """This method validates the conf_mgr.__init__ method
        when invoked with a path to a file that does not exist
        """
        conf = ConfManager(env_file=".env")
        self.case.assertIsNone(conf.env_file, "env_file")
        self.assert_dict(
            expected=FileLoggerConf(sink=conf_mgr.defaults_logging_conf.get("sink")),
            result=conf.logging_conf,
            msg="logging_conf",
        )


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

if __name__ == "__main__":
    pytest.main()
