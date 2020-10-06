"""
Author:Viktoria Denys
Program:string_functions.py
function multiply_string() that takes a string message
and a number n and returns the string with message printed n times

"""

def multiply_string(s, n):
    """takes a string message and a number n and returns the string with message printed n times."""
    s = s * n
    return s  # returns message printed n times


if __name__ == '__main__':

    string = input("Please enter your name:")  # prompts name
    try:
        number = int(input("How many times you want your name  printed?(between 1-9):"))
        # prompts number between 1 and 9.
        if 1 > number or number > 9:
            print("Please enter number between 1-9")
            number = int(input("How many times you want your name printed?(between 1-9):"))

    except ValueError as err:
        print("ValueError found!!")
    else:
        print(multiply_string(string, number))  # calls to function and print result
