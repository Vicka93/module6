"""
Author:Viktoria Denys
Program:inner_functions_assignment.py

accepts a list of measurements for a rectangle and returns a string with perimeter and area

"""

import unittest
from more_functions import inner_functions_assignment as inner

class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(inner.measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(inner.measurements([3.5]), "Perimeter = 14.0 Area = 12.25")

    def test_measurements_too_many_values(self):
        with self.assertRaises(IndexError):
            inner.measurements([2.1, 3.4, 4])

    def test_measurements_no_measurements(self):
        with self.assertRaises(IndexError):
            inner.measurements([])


if __name__ == '__main__':
    unittest.main()
