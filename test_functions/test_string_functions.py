"""
Author:Viktoria Denys
Program:string_functions.py
function multiply_string() that takes a string message
and a number n and returns the string with message printed n times

"""

import unittest
from more_functions import string_functions


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("AyahAyahAyah", string_functions.multiply_string("Ayah", 3))


if __name__ == '__main__':
    unittest.main()
