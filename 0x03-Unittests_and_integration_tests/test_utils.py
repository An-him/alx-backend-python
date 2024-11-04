#!/usr/bin/python3
import unittest
from parameterized import parameterized
from utils access_nested_map
from typing import Dict, Tuple, Any

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", ), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

        def test_access_nested_map(self, nested_map: Dict[str, Any], path: Tuple[str, ...], expected: Any) -> None:
            self.assertEqual(access_nested_map(nested_map, path), expected)
