"""
Author:Viktoria Denys
Program:validate_input_in_functions.py

takes a test_name, test_score,
and invalid_message that validates the test_score, then prints valid input as 'Test name: ##'.

"""


def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    """takes a test_name, test_score,
    and invalid_message that validates the test_score,
    then prints valid input as 'Test name: ##'."""
    #print("{}: {}".format(test_name, test_score))
    return "{}: {}".format(test_name, test_score)


if __name__ == '__main__':
    score_input("test1", 45)
