"""
Imaginary Coding Interview by Timothy Eden
Date Last Modified: September 16, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/3A3mHS5B3NNZddQL2
"""


def interview(lst, tot):
    """
    Before evaluating the length of time spent on individual questions, there are 2 simple ways the candidate can be
    immediately disqualified; not answering all 8 questions, or having a total time of over 120 minutes. The function
    begins by evaluating these two conditions, and if either one is true, then it can return "disqualified" without
    having to run any other code. If the function continues, we start by initializing an i variable which tracks the
    index of the item being evaluated in the list, starting from 0 and incrementing by 1 each time. Now, in our list, we
    know that the items in positions 0 and 1 represent the time spent answering "very easy" questions, 2 and 3 are
    "easy", 4 and 5 are "medium", and 6 and 7 are "hard". Given this, our for loop has 4 if-statements which account for
    all of these possibilities, and within each if-statement is another one which determines whether the candidate spent
    too much time answering the question based on the difficulty. If so, the candidate is disqualified and the function
    can stop running. If the function makes it all the way to the end without returning "disqualified", then it returns
    "qualified".
    """
    if len(lst) != 8:  # candidate didn't answer every question
        return 'disqualified'
    if tot > 120:
        return 'disqualified'
    i = 0
    for q in lst:
        if i in [0, 1]:  # first 2 are very easy
            if q > 5:
                return 'disqualified'
        if i in [2, 3]:  # next 2 are easy
            if q > 10:
                return 'disqualified'
        if i in [4, 5]:  # next 2 are medium
            if q > 15:
                return 'disqualified'
        if i in [6, 7]:  # final 2 are hard
            if q > 20:
                return 'disqualified'
        i += 1
    return 'qualified'


def main():
    assert interview([5, 5, 10, 10, 15, 15, 20, 20], 120) == 'qualified'
    assert interview([2, 3, 8, 6, 5, 12, 10, 18], 120) == 'qualified'
    assert interview([2, 3, 8, 6, 5, 12, 10, 18], 64) == 'qualified'
    assert interview([5, 5, 10, 10, 25, 15, 20, 20], 120) == 'disqualified'
    assert interview([5, 5, 10, 10, 15, 15, 20], 120) == 'disqualified'
    assert interview([5, 5, 10, 10, 15, 15, 20, 20], 130) == 'disqualified'
    assert interview([5, 5, 10, 10, 15, 20, 50], 160) == 'disqualified'
    assert interview([5, 5, 10, 10, 15, 15, 40], 120) == 'disqualified'
    assert interview([10, 10, 15, 15, 20, 20], 150) == 'disqualified'
    assert interview([5, 5, 10, 20, 15, 15, 20, 20], 140) == 'disqualified'


if __name__ == '__main__':
    main()
