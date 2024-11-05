#!/usr/bin/env python3
"""
unittest for utils
"""
import unittest
import unittest.mock
import utils
from parameterized import parameterized
from typing import Dict, Tuple, Union
import requests


class TestAccessNestedMap(unittest.TestCase):
    """test access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map: Dict,
                               path: Tuple, expected: Union[int, Dict]):
        """test access nested map"""
        self.assertEqual(utils.access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map: Dict, path: Tuple):
        """test access nested map with exception"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """test get json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """test get json"""
        attrs = {"json.return_value": test_payload}
        with unittest.mock\
                .patch(
                    "requests.get",
                    return_value=unittest.mock.Mock(**attrs)) as req_get:
            self.assertEqual(utils.get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)
