"""
The goal of this module is to implement the base class used by all test classes
with common methods.
"""
# pylint: disable=E0611,R0911
#        E0611: No name 'BaseModel' in module 'pydantic' (no-name-in-module)
#        R0911: Too many return statements (10/6) (too-many-return-statements)
# ───────────────────────────────────────────────────── imports ────────────────────────────────────────────────────── #
import unittest
from collections import OrderedDict
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Optional, Union, List

import pytest
from loguru import logger
from pydantic import BaseModel, BaseSettings
from pydantic.fields import ModelField

from evoml_python_commons.conf.base_data_types import PropertyBaseModel, BaseModelWithAlias

# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #
#                                                   Base Test Class                                                    #
# ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────── #

DictType = Union[Dict, BaseModel, BaseSettings, PropertyBaseModel, BaseModelWithAlias]


class BaseTest:
    """Base Tests Class"""

    case = unittest.TestCase()
    method: str = "Unknown"

    # --------------------------------------------------------------------------------------------------

    @classmethod
    def setup_class(cls):
        """Configuration called when initializing the class"""

    @classmethod
    def teardown_class(cls):
        """Configuration called when destroying the class"""

    def setup_method(self, method):
        """Configuration called for every method"""
        self.method = method.__name__

    def teardown_method(self, method):
        """Configuration called at the end of the method execution"""

    # --------------------------------------------------------------------------------------------------

    @staticmethod
    def join_values(values: List[str], union: str = "") -> str:
        """Joins all the strings in the list by means of the string
        indicated in "union", filtering those null or empty values.
        """
        return union.join(list(filter(lambda value: value, values)))

    # --------------------------------------------------------------------------------------------------

    def serialize_data(self, data: Any, by_alias: bool = False, date_format: str = "%Y-%m-%d %H:%M:%S") -> Any:
        """Serialize any type of data so that it can be compared"""
        kwargs = dict(date_format=date_format, by_alias=by_alias)
        if isinstance(data, ModelField):
            return self.serialize_data(
                data=dict(name=data.name, alias=data.alias, type=data.outer_type_, required=data.required),
                by_alias=by_alias,
            )
        if isinstance(data, Dict):
            return {key: self.serialize_data(data=value, **kwargs) for key, value in data.items()}  # type: ignore
        if isinstance(data, PropertyBaseModel):
            return self.serialize_data(data=data.dict_prop())
        if isinstance(data, BaseModel):
            return self.serialize_data(data=data.dict())
        if isinstance(data, (list, tuple)):
            return [self.serialize_data(data=value, **kwargs) for value in data]  # type: ignore
        if isinstance(data, type):
            return str(data)
        if isinstance(data, Path):
            return str(data)
        if isinstance(data, datetime):
            return data.strftime(date_format)
        if isinstance(data, Enum):
            return data.value
        return data

    def sorted_serialize_data(self, data: Any, by_alias: bool = False, serialized: bool = True) -> Any:
        """Serialize and sort any type of data so that it can be compared"""
        serialized_data = self.serialize_data(data=data, by_alias=by_alias) if serialized else data
        if isinstance(data, dict):
            return dict(OrderedDict(sorted(serialized_data.items())))
        if isinstance(data, list):
            return sorted(serialized_data)
        return serialized_data

    # --------------------------------------------------------------------------------------------------

    def assert_dict(
        self,
        expected: DictType,
        result: DictType,
        serialized: bool = True,
        by_alias: bool = False,
        msg: Optional[str] = None,
    ):
        """Serialize the dictionaries and check that they are equal"""
        expected_serialized = self.sorted_serialize_data(data=expected, by_alias=by_alias, serialized=serialized)
        result_serialized = self.sorted_serialize_data(data=result, by_alias=by_alias, serialized=serialized)
        try:
            self.case.assertDictEqual(expected_serialized, result_serialized, msg)
        except AssertionError as error:
            logger.error(f"\n - expected: {expected_serialized}" f"\n - result  : {result_serialized}")
            raise error

    def assert_list(self, expected: List, result: List, by_alias: bool = False, msg: Optional[str] = None):
        """Serialize the lists and check that they are equal"""
        expected_serialized = self.serialize_data(data=expected, by_alias=by_alias)
        result_serialized = self.serialize_data(data=result, by_alias=by_alias)
        try:
            self.case.assertListEqual(expected_serialized, result_serialized, msg)
        except AssertionError as error:
            logger.error(f"\n - expected: {expected_serialized}" f"\n - result  : {result_serialized}")
            raise error

    def assert_dict_diff(self, expected: DictType, result: DictType, by_alias: bool = False, msg: str = None):
        """Serialize the dictionaries and check that they are not equal"""
        with pytest.raises(AssertionError):
            self.assert_dict(expected=expected, result=result, by_alias=by_alias, msg=msg)
            assert True

    def assert_list_diff(self, expected: List, result: List, by_alias: bool = False, msg: str = None):
        """Serialize the list and check that they are not equal"""
        with pytest.raises(AssertionError):
            self.assert_list(expected=expected, result=result, by_alias=by_alias, msg=msg)
            assert True
