"""
Up the Hill, Down the Hill by Timothy Eden
Date Last Modified: September 13, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/NYEaXXCnSj9jteNWA
"""


def ave_spd_old(up_time, up_spd, down_spd):
    """
    Original version of ave_spd, the new version contains a more concise calculation for the ave variable.
    """
    up_spd = up_spd / 60
    down_spd = down_spd / 60
    hill_length = up_spd * up_time
    down_time = hill_length / down_spd
    total_time = up_time + down_time
    ave_min = ((up_time / total_time) * up_spd) + ((down_time / total_time) * down_spd)
    ave = ave_min * 60
    return ave


def ave_spd(up_time, up_spd, down_spd):
    """
    Since time is given in minutes and speed is given in miles per hour, we must convert everything to the same unit. I
    chose to convert everything to minutes (the smallest unit), although alternatively hours could be used. The missing
    information needed is the length of the hill in miles, and the time spent going down the hill, so these are
    calculated. Since the total distance traveled is the length of the hill twice, dividing this by the total time
    spent traveling gives us our average speed. As we converted everything to miles per minute before, we must multiply
    the result by 60, as the exercise expects the result in miles per hour.
    """
    up_spd = up_spd / 60
    down_spd = down_spd / 60
    hill_length = up_spd * up_time
    down_time = hill_length / down_spd
    total_time = up_time + down_time
    ave = ((hill_length * 2) / total_time) * 60
    return ave


def main():
    assert ave_spd(18, 10, 30) == 15
    assert ave_spd(18, 20, 60) == 30
    assert ave_spd(30, 10, 30) == 15
    assert ave_spd(30, 8, 24) == 12


if __name__ == '__main__':
    main()
