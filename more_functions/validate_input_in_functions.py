"""
Author:Viktoria Denys
Program:validate_input_in_functions.py

takes a test_name, test_score,
and invalid_message that validates the test_score, then prints valid input as 'Test name: ##'.

"""


def score_input(test_name, test_score=0, invalid_message="Invalid test score, try again!"):
    """
     Function that takes a test_name, test_score and prints valid input as 'Test name: ##'.
    :param test_name: The name of the test
    :type test_name:String
    :param test_score:A value between 0-100
    :type test_score: Int
    :param invalid_message:message displayed when invalid score provided
    :type invalid_message: String
    :return:formatted string with test name and score
    :rtype: String
    """
    try:
        if 0 <= test_score <= 100:
           # print("{}: {}".format(test_name, test_score))
           return "{}: {}".format(test_name, test_score)
        else:
            return invalid_message
    except TypeError:
        raise TypeError


if __name__ == '__main__':
    try:
        print(score_input("test1", "45"))
    except TypeError:
        print("not a valid score!")
