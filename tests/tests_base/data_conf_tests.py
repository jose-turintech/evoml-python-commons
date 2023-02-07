"""
This module defines the file directory structure
"""
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
from pathlib import Path

from evoml_python_commons.conf.base_data_types import PropertyBaseModel

from tests import TESTS_PATH


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                  Data Configuration                                                  #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


class DataConfTests(PropertyBaseModel):
    """Configuration class of the Tests' Data.

    data
    ├── expected
    │   ├── integration/
    │   └── unit/
    └── input/
    """

    data_path: Path

    # --------------------------------------------------------------------------------------------------

    @property
    def input_path(self) -> Path:
        return self.data_path.joinpath("input")

    def input(self, file_name: str):
        return self.input_path.joinpath(file_name)

    # --------------------------------------------------------------------------------------------------

    @property
    def expected_path(self) -> Path:
        return self.data_path.joinpath("expected")

    @property
    def expected_integration(self) -> Path:
        return self.expected_path.joinpath("integration")

    @property
    def expected_unit(self) -> Path:
        return self.expected_path.joinpath("unit")

    # --------------------------------------------------------------------------------------------------


# ────────────────────────────────────────────── DataConfTests instance ────────────────────────────────────────────── #

data_mgr: DataConfTests = DataConfTests(data_path=TESTS_PATH.joinpath("data"))
