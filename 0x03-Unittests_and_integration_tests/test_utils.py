#!/usr/bin/env python3
"""
unittest for utils
"""
import unittest
import utils


class TestAccessNestedMap(unittest.TestCase):
    def test_access_nested_map(self):
        self.assertEqual(utils.access_nested_map({"a": 1}, ["a"]), 1)
        self.assertEqual(utils.access_nested_map({"a": {"b": 2}},
                                                 ["a"]),  {"b": 2})
        self.assertEqual(utils.access_nested_map({"a": {"b": 2}},
                                                 ["a", "b"]), 2)
