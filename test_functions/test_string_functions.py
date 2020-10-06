import unittest
from more_functions import string_functions


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("AyahAyahAyah", string_functions.multiply_string("Ayah", 3))


if __name__ == '__main__':
    unittest.main()
