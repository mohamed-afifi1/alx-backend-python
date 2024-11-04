#!/usr/bin/env python3
"""
unittest for utils
"""
import unittest
import utils
from parameterized import parameterized
from typing import Dict, Tuple, Union


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
