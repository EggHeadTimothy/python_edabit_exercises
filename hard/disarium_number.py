"""
Disarium Number by Timothy Eden
Date Last Modified: September 15, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/yvJbdkmKHvCNtcZy9
"""


def is_disarium(n):
    """
    In order to separate n into its individual digits, n must be briefly converted into a string. Then, for each
    character in the string n, the character is converted back to an integer and added to a list of the digits. After
    this, n is converted back to an integer. The sum of raised digits is calculated by looping through each integer in
    the digits list, taking it to the power of its position, and adding this to an accumulator variable which is then
    compared to n to determine whether the function should return True or False.
    """
    n = str(n)
    digits = []
    for digit in n:
        digit = int(digit)
        digits.append(digit)
    n = int(n)
    sord = 0  # acronym for 'sum of raised digits'
    pos = 1
    for digit in digits:
        sord += digit ** pos
        pos += 1
    if sord == n:
        return True
    else:
        return False


def main():
    assert is_disarium(6) is True
    assert is_disarium(75) is False
    assert is_disarium(135) is True
    assert is_disarium(466) is False
    assert is_disarium(372) is False
    assert is_disarium(175) is True
    assert is_disarium(1) is True
    assert is_disarium(696) is False
    assert is_disarium(876) is False
    assert is_disarium(89) is True
    assert is_disarium(518) is True
    assert is_disarium(598) is True


if __name__ == '__main__':
    main()
