"""
Friday the 13th by Timothy Eden
Date Last Modified: September 17, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/Xkc2iAjwCap2z9N5D
"""

import datetime


def has_friday_13(month, year):
    """
    Given the month, we're looking at the 13th of that month to see whether it's a Friday. So, the date variable is
    initialized to the 13th of that month. The date.weekday() method returns 4 if the weekday of the given date is
    Friday. If this is the case, the function returns True, otherwise it returns False.
    """
    date = datetime.datetime(year, month, 13)
    if date.weekday() == 4:
        return True
    else:
        return False


def main():
    assert has_friday_13(3, 2020) is True
    assert has_friday_13(10, 2017) is True
    assert has_friday_13(1, 1985) is False
    assert has_friday_13(5, 1619) is False
    assert has_friday_13(6, 1614) is True
    assert has_friday_13(8, 1767) is False
    assert has_friday_13(6, 1589) is False
    assert has_friday_13(2, 2015) is True
    assert has_friday_13(3, 2015) is True
    assert has_friday_13(11, 2015) is True
    assert has_friday_13(2, 1759) is False
    assert has_friday_13(8, 1612) is False
    assert has_friday_13(8, 1612) is False
    assert has_friday_13(10, 2029) is False
    assert has_friday_13(1, 1590) is False


if __name__ == '__main__':
    main()
