"""
Length of Number by Timothy Eden
Date Last Modified: October 3, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/2zKetgAJp4WRFXiDT
"""


def number_length(num):
    """
    We convert num to a string, initialize an accumulator variable for the length, then for each character in num, we
    add 1 to the accumulator.
    """
    length = 0
    str_num = str(num)
    for _ in str_num:
        length += 1
    return length


def main():
    assert number_length(10) == 2
    assert number_length(5000) == 4
    assert number_length(0) == 1
    assert number_length(4039182) == 7
    assert number_length(9999999999999999) == 16
    assert number_length(1) == 1
    assert number_length(777777777777777777777777777777) == 30


if __name__ == '__main__':
    main()
