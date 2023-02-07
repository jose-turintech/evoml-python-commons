# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
from pathlib import Path

from evoml_python_commons import ConfManager
from evoml_python_commons.conf.logger_conf import FileLoggerConf

from tests.tests_base.base_test import BaseTest


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                   Base Test Class                                                    #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


class BaseTestConfManager(BaseTest):
    """Base Tests Class of ConfManager tests"""

    @property
    def env_file(self) -> Path:
        """Environment configuration file"""
        raise NotImplementedError

    @property
    def expected_init_logging_conf(self) -> FileLoggerConf:
        """Expected logging configuration when instantiating a
        ConfManager with the environment configuration file.
        """
        raise NotImplementedError

    # --------------------------------------------------------------------------------------------------

    def test_conf_mgr_init(self):
        """This method validates the conf_mgr.__init__ method
        when is invoked with an existing environment file
        """
        conf = ConfManager(env_file=self.env_file)
        self.case.assertEqual(str(self.env_file), conf.env_file)
        self.assert_dict(expected=self.expected_init_logging_conf, result=conf.logging_conf, msg="logging_conf")
