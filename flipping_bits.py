"""
Flipping Bits by Timothy Eden
Date Last Modified: September 15, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/z39yXccJGLAy3BDNX
"""


def to_binary(integer):
    """
    A method of converting a base-10 number to binary is by dividing the number by 2, getting the remainder (either 0 or
    1), adding the remainder of the equation to the binary result (this is built from right-to-left), and repeating this
    process until dividing our base-10 number by 2 brings it below 1. This function builds it out as a string using this
    method.
    """
    binary = ''
    while integer >= 1:
        remainder = integer % 2
        binary = str(remainder) + binary
        integer = integer // 2
    return binary


def to_decimal(binary):
    """
    The base-10 number represented in binary is the sum of each binary digit times 2 to the power of its position (going
    from right-to-left). Since Python iterates from left-to-right, we first reverse the string containing the binary
    number. We then initialize a variable for the decimal number, which starts at 0. The variable i is used to track
    the position, starting at 0 and incrementing by 1 for each iteration of the loop. For each digit in the binary
    number, the binary digit (either 0 or 1) is multiplied by 2 to the power of its position, and this is added to the
    decimal variable.
    """
    binary = (str(binary))[::-1]  # reverses the string
    decimal = 0
    i = 0
    for digit in binary:
        decimal += int(digit) * (2 ** i)
        i += 1
    return decimal


def make_32_bit(binary):
    """
    In this project, the desired length of each binary number is 32 bits, so if our binary number is less than 32
    digits, we must add zeros to the left in order to pad the number. This function determines the length of the binary
    number, determines how many extra zeros are needed, creates a string containing this many zeros, then adds this
    string of zeros to the left of the original binary number, ensuring that the length of it is 32 bits.
    """
    length = len(binary)
    needed = 32 - length
    zeros = ''
    for i in range(needed):
        zeros += '0'
    binary = zeros + binary
    return binary


def flipping_bits(n):
    """
    The helper functions written for this function take care of converting the variable n to binary and adding the
    necessary padding (as well as converting it to a string). Then, a new empty string is created, and for each digit
    in the original binary number, if the digit is 0, the digit 1 is added to the new string, and vice versa. After a
    string has been created representing the binary number with all bits flipped, this is converted back into a
    decimal number.
    """
    n = to_binary(n)
    n = make_32_bit(n)
    new_binary = ''
    for digit in n:
        if digit == '0':
            new_binary += '1'
        if digit == '1':
            new_binary += '0'
    n = int(new_binary)
    n = to_decimal(n)
    return n


def main():
    assert flipping_bits(4) == 4294967291
    assert flipping_bits(2147483647) == 2147483648
    assert flipping_bits(1) == 4294967294
    assert flipping_bits(0) == 4294967295
    assert flipping_bits(802743475) == 3492223820
    assert flipping_bits(35601423) == 4259365872
    assert flipping_bits(123456) == 4294843839
    assert flipping_bits(4) == 4294967291


if __name__ == '__main__':
    main()
