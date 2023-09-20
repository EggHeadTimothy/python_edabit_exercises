"""
Identity Matrix by Timothy Eden
Date Last Modified: September 20, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/QN4RMpAnktNvMCWwg
"""


def id_mtrx(n):
    """
    Before going through logic to actually construct the identity matrix, we first deal with 2 possibilities; that n is
    not an integer (in which we simply return 'Error'), or that n is 0, in which we just return an empty list.

    Otherwise, we must construct our matrix. The variable nabs contains the absolute value of n, which accounts for the
    fact that n might be a negative number (for things like determining the number of rows and length of each row, which
    should always be the absolute value of n). Now, for each row, there will be one instance of the number 1 as opposed
    to 0, and the desired position of this 1 will follow one of two patterns; if n is positive, it starts at position 0
    and will increment with each new row, and if n is negative, it starts at the highest position (nabs - 1), and
    decrements with each new row.

    The number of rows and the length of each row will be determined using nabs. While creating each row we keep track
    of the current position of the number we're appending, and the desired position of the 1. If our current position
    is the desired position, we append 1 instead of 0, otherwise we append 0. When the row is done, it is appended to
    mtrx (a nested list containing each row as a list).
    """
    if type(n) != int:
        return 'Error'
    elif n == 0:
        return []
    else:
        mtrx = []
        nabs = abs(n)
        if n > 0:
            desired_pos = 0
        else:
            desired_pos = nabs - 1
        for i in range(nabs):
            row = []
            pos = 0
            for j in range(nabs):
                if pos == desired_pos:
                    row.append(1)
                else:
                    row.append(0)
                pos += 1
            mtrx.append(row)
            if n > 0:
                desired_pos += 1
            else:
                desired_pos -= 1
        return mtrx


def main():
    assert id_mtrx(1) == [
        [1]
    ]
    assert id_mtrx(2) == [
        [1, 0],
        [0, 1]
    ]
    assert id_mtrx(3) == [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    assert id_mtrx(4) == [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    assert id_mtrx(-6) == [
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0]
    ]
    assert id_mtrx('edabit') == 'Error'


if __name__ == '__main__':
    main()
