"""
Pentagonal Number by Timothy Eden
Date Last Modified: September 17, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/st8mDxreMcuWxuz8c
"""


def pentagonal(num):
    """
    For each iteration after the first, the number of dots being added increments by 5. The variable to_add is
    initialized at 5, and increments by 5 each time it is added to the number of dots.
    """
    dots = 1
    to_add = 5
    for i in range(num - 1):
        dots += to_add
        to_add += 5
    return dots


def main():
    assert pentagonal(1) == 1
    assert pentagonal(3) == 16
    assert pentagonal(8) == 141
    assert pentagonal(10) == 226
    assert pentagonal(15) == 526
    assert pentagonal(33) == 2641
    assert pentagonal(43) == 4516
    assert pentagonal(13) == 391
    assert pentagonal(50) == 6126
    assert pentagonal(62) == 9456
    assert pentagonal(21) == 1051


if __name__ == '__main__':
    main()
