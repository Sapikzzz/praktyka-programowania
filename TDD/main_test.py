import unittest
from main import *

class TestMain(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_one_number(self):
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("2"), 2)

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)
        self.assertEqual(add("2,3"), 5)

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3"), 6)
        self.assertEqual(add("3,4,5,6"), 18)

    def test_negative_number(self):
        self.assertEqual(add("-1,2"), -1)

    def test_many_delimiters(self):
        self.assertEqual(add("1,2,"), -1)

    def test_different_delimiters_twp_numbers(self):
        self.assertEqual(add("1\n2"), 3)
        self.assertEqual(add("1\n2\n3"), 6)
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("1\n2\n3\n"), -1)
        self.assertEqual(add("1,\n"), -1)
