"""
Author:Viktoria Denys
Program:validate_input_in_functions.py

takes a test_name, test_score,
and invalid_message that validates the test_score, then prints valid input as 'Test name: ##'.

"""
import unittest
from more_functions import validate_input_in_functions as valid_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual("Python1!: 0", valid_input.score_input("Python1!"))

    def test_score_input_test_score_valid(self):
        self.assertEqual("Python2!: 97", valid_input.score_input("Python2!", 97))

    def test_score_input_test_score_below_range(self):
        self.assertEqual("Invalid test score, try again!", valid_input.score_input("Python3!", -1))

    def test_score_input_test_score_above_range(self):
        self.assertEqual("Invalid test score, try again!", valid_input.score_input("Python4!", 101))

    def test_test_score_non_numeric(self):
        with self.assertRaises(TypeError):
            valid_input.score_input("Python5!", "hundred")

    def test_score_input_invalid_message(self):
        self.assertEqual("Not  acceptable score try again!", valid_input.score_input("Python6!", 101,
                                                                                     "Not  acceptable score "
                                                                                     "try again!"))


if __name__ == '__main__':
    unittest.main()
