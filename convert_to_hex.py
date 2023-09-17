"""
Convert to Hex by Timothy Eden
Date Last Modified: September 17, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/g6yjSfTpDkX2STnSX
"""

hexadecimal_letters = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}


def to_hexadecimal(number):
    """
    A method of converting a base-10 number to hexadecimal is by dividing the number by 16, getting the remainder,
    adding the remainder of the equation to the hexadecimal result (this is built from right-to-left), and repeating
    this process until dividing our base-10 number by 16 brings it below 1. This function builds it out as a string
    using this method.

    For numbers 10 through 15, a dictionary is accessed translating these numbers to their respective hexadecimal
    representations.
    """
    hexadecimal = ''
    while number >= 1:
        remainder = number % 16
        if remainder in [10, 11, 12, 13, 14, 15]:
            remainder = hexadecimal_letters[remainder]
        hexadecimal = str(remainder) + hexadecimal
        number = number // 16
    return hexadecimal


def convert_to_hex(txt):
    """
    First, an empty string is created to store our result. We must keep track of whether we're at the final index in
    order to determine whether a space should be added after our hexadecimal digit. This is kept track of using the
    index variable which starts at 0 and increments by 1 after each iteration, and the final_index variable which it is
    compared to. For every character in the original text, the ASCII value is determined using the ord() function, and
    this ASCII value is then translated into hexadecimal using the helper function to_hexadecimal(). It is then added
    onto the string.
    """
    hexadecimal = ''
    index = 0
    final_index = len(txt) - 1
    for character in txt:
        if index != final_index:
            ascii_num = ord(character)
            hex_digit = to_hexadecimal(ascii_num)
            hexadecimal += '{} '.format(hex_digit)
        else:
            ascii_num = ord(character)
            hex_digit = to_hexadecimal(ascii_num)
            hexadecimal += '{}'.format(hex_digit)
        index += 1
    return hexadecimal


def main():
    assert convert_to_hex("Big Boi") == "42 69 67 20 42 6f 69"
    assert convert_to_hex("Marty Poppinson") == "4d 61 72 74 79 20 50 6f 70 70 69 6e 73 6f 6e"
    assert convert_to_hex("abcdefghi") == "61 62 63 64 65 66 67 68 69"
    assert convert_to_hex("oh dear") == "6f 68 20 64 65 61 72"
    assert convert_to_hex("i hate C#") == "69 20 68 61 74 65 20 43 23"


if __name__ == '__main__':
    main()
