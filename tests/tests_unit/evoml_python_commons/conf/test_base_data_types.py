"""
This module aims to implement the tests of the base_data_types module
"""
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
from pathlib import Path
from typing import Type

import pytest
from pydantic import Field

from evoml_python_commons.conf.base_data_types import BaseModelWithAlias, PropertyBaseModel

from tests.tests_base.base_test import BaseTest


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                      Test Class                                                      #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #


class Example1(BaseModelWithAlias):
    id: str = Field("1234567", alias="_id")
    field_alias: Type = str
    field_my_alias: str = Field("my alias", alias="myAlias")
    field1: str = "field1"
    fieldCamelCase: str = "camel case"


class Example2(PropertyBaseModel):
    root_path: Path = Path(".")

    @property
    def folder_1(self):
        return self.root_path.joinpath("folder1")


class Example3(Example2):
    @property
    def folder_2(self):
        return self.root_path.joinpath("folder2")

    @property
    def folder_3(self):
        return self.folder_1.joinpath("folder3")


class TestBaseDataTypes(BaseTest):
    """conf.base_data_types.py testing class"""

    example1 = Example1()
    example1_expected_py = dict(
        id="1234567", field_alias=str, field_my_alias="my alias", field1="field1", fieldCamelCase="camel case"
    )
    example1_expected_json = dict(
        _id="1234567", fieldAlias=str, myAlias="my alias", field1="field1", fieldCamelCase="camel case"
    )

    # --------------------------------------------------------------------------------------------------
    #                                      BaseModelWithAlias class
    # --------------------------------------------------------------------------------------------------

    def test_base_model_with_alias_dict(self):
        """This method validates the BaseModelWithAlias.dict() method"""
        self.assert_dict(
            expected=self.example1_expected_json, result=self.example1.dict(), serialized=False, msg="dict()"
        )
        self.assert_dict(
            expected=self.example1_expected_json,
            result=self.example1.dict(by_alias=True),
            serialized=False,
            msg="dict(by_alias=True)",
        )
        self.assert_dict(
            expected=self.example1_expected_py,
            result=self.example1.dict(by_alias=False),
            serialized=False,
            msg="dict(by_alias=False)",
        )

    def test_base_model_with_alias_dict_py(self):
        """This method validates the BaseModelWithAlias.dict_py() method"""
        self.assert_dict(
            expected=self.example1_expected_py, result=self.example1.dict_py(), serialized=False, msg="dict_py()"
        )
        self.assert_dict(
            expected=self.example1_expected_py,
            result=self.example1.dict_py(by_alias=True),
            serialized=False,
            msg="dict_py(by_alias=True)",
        )
        self.assert_dict(
            expected=self.example1_expected_py,
            result=self.example1.dict_py(by_alias=False),
            serialized=False,
            msg="dict_py(by_alias=False)",
        )

    def test_base_model_with_alias_dict_json(self):
        """This method validates the BaseModelWithAlias.dict_json() method"""
        self.assert_dict(
            expected=self.example1_expected_json, result=self.example1.dict_json(), serialized=False, msg="dict_json()"
        )
        self.assert_dict(
            expected=self.example1_expected_json,
            result=self.example1.dict_json(by_alias=True),
            serialized=False,
            msg="dict_json(by_alias=True)",
        )
        self.assert_dict(
            expected=self.example1_expected_json,
            result=self.example1.dict_json(by_alias=False),
            serialized=False,
            msg="dict_json(by_alias=False)",
        )

    def test_base_model_with_alias_update(self):
        """This method validates the BaseModelWithAlias.update() method"""
        example = Example1()
        expected = self.example1_expected_json

        self.assert_dict(expected=expected, result=example.dict_json(), serialized=False, msg="original")

        example.update(data=dict(id="updatedByKey"))
        expected["_id"] = "updatedByKey"
        self.assert_dict(expected=expected, result=example.dict_json(), serialized=False, msg="updated by key")

        example.update(data=dict(_id="updatedByAlias"))
        expected["_id"] = "updatedByAlias"
        self.assert_dict(expected=expected, result=example.dict_json(), serialized=False, msg="updated by alias")

    # --------------------------------------------------------------------------------------------------
    #                                      PropertyBaseModel class
    # --------------------------------------------------------------------------------------------------

    def test_property_base_model_dict(self):
        """This method validates the PropertyBaseModel.dict() method"""

        expected = dict(root_path=Path("."))

        example2 = Example2()
        self.assert_dict(expected=expected, result=example2.dict(), serialized=False, msg="example2")

        example3 = Example3()
        self.assert_dict(expected=expected, result=example3.dict(), serialized=False, msg="example3")

    def test_property_base_model_dict_prop(self):
        """This method validates the PropertyBaseModel.dict_prop() method"""

        example2 = Example2()
        expected2 = dict(root_path=Path("."), folder_1=Path(".").joinpath("folder1"))
        self.assert_dict(expected=expected2, result=example2.dict_prop(), serialized=False, msg="example2")

        example3 = Example3()
        expected3 = dict(
            root_path=Path("."),
            folder_1=Path(".").joinpath("folder1"),
            folder_2=Path(".").joinpath("folder2"),
            folder_3=Path(".").joinpath(*["folder1", "folder3"]),
        )
        self.assert_dict(expected=expected3, result=example3.dict_prop(), serialized=False, msg="example3")

        expected_include = dict(folder_3=expected3.pop("folder_3"))
        self.assert_dict(
            expected=expected3, result=example3.dict_prop(exclude={"folder_3"}), serialized=False, msg="exclude"
        )
        self.assert_dict(
            expected=expected_include, result=example3.dict_prop(include={"folder_3"}), serialized=False, msg="include"
        )


# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

if __name__ == "__main__":
    pytest.main()
