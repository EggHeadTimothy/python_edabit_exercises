"""
Concert Seats by Timothy Eden
Date Last Modified: October 3, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/xbjDMxzpFcsAWKp97
"""


def get_columns(seats):
    """
    This function takes in a nested list representing rows, and returns the columns.
    """
    columns = []
    index = 0
    for _ in seats:
        column = []
        for row in seats:
            column.append(row[index])
        columns.append(column)
        index += 1
    return columns


def can_see_stage(seats):
    """
    This function starts by using the helper function get_columns to convert the rows to columns. Then, for each number
    in each column, we check if it's less than or equal to the previous number (unless it's the first number in the
    column, in which case nothing happens). If this condition is true, the function immediately stops to return False.
    If it iterates over every column and never returns False, then we reach the final "return True" statement.
    """
    columns = get_columns(seats)
    for column in columns:
        index = 0
        for number in column:
            if index == 0:
                pass
            else:
                prev_num = column[index - 1]
                if number <= prev_num:
                    return False
            index += 1
    return True


def main():
    assert can_see_stage(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]) is True

    assert can_see_stage(
        [[1, 2, 2],
         [1, 2, 3],
         [4, 4, 4]]) is False

    assert can_see_stage(
        [[1, 1, 2],
         [5, 2, 3],
         [4, 4, 4]]) is False

    assert can_see_stage(
        [[1, 1, 2],
         [5, 2, 3],
         [6, 4, 4]]) is True

    assert can_see_stage(
        [[0, 0, 0],
         [1, 1, 1],
         [2, 2, 2]]) is True

    assert can_see_stage(
        [[2, 0, 0],
         [1, 1, 1],
         [2, 2, 2]]) is False

    assert can_see_stage(
        [[1, 0, 0],
         [1, 1, 1],
         [2, 2, 2]]) is False

    assert can_see_stage(
        [[1, 2, 3, 2, 1, 1],
         [2, 4, 4, 3, 2, 2],
         [5, 5, 5, 5, 4, 4],
         [6, 6, 7, 6, 5, 5]]) is True

    assert can_see_stage(
        [[1, 2, 3, 2, 1, 1],
         [2, 4, 4, 3, 2, 2],
         [5, 5, 5, 10, 4, 4],
         [6, 6, 7, 6, 5, 5]]) is False


if __name__ == '__main__':
    main()
