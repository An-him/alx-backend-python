#!/usr/bin/python3
import unittest
from parameterized import parameterized
from utils access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map():
        self.assertEqual(access_nested_map(nested_map, path), expected)
