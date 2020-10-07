"""
Author:Viktoria Denys
Program:inner_functions_assignment.py

accepts a list of measurements for a rectangle and returns a string with perimeter and area

"""


def measurements(rect_measure):
    perimeter_value = 0.0
    area_value = 0.0

    def area(a_measure):
        if len(a_measure) == 1:
            return a_measure[0]*a_measure[0]
        elif len(a_measure) == 2:
            return a_measure[0]*a_measure[1]
        else:
            raise IndexError

    def perimeter(p_measure):
        if len(p_measure) == 1:
            return p_measure[0]*4
        elif len(p_measure) == 2:
            return p_measure[0]*2 + p_measure[1] * 2
        else:
            raise IndexError
    try:
        area_value = area(rect_measure)
        perimeter_value = perimeter(rect_measure)
    except IndexError:
        raise IndexError
    return "Perimeter = {} Area = {}".format(perimeter_value, area_value)


if __name__ == '__main__':
    try:
        print(measurements([2.1, 3.4]))
    except IndexError:
        print("Enter one or two measurements for area and perimeter!")