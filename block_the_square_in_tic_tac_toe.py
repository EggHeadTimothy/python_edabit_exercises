"""
Block the Square in Tic Tac Toe by Timothy Eden
Date Last Modified: September 24, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/bWNZ3y98NwZRKk5rj
"""


def block_player(a, b):
    """
    The list wins contains eight lists, each containing one of the possible combos for winning. We iterate through
    each nested list in this list to see which one contains both a and b, and assign this to a variable called combo.
    Then, we remove a and b from combo, and the only remaining item in combo is our answer.
    """
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    combo = []
    index = 0
    for i in wins:
        if a in i and b in i:
            combo = wins[index]
            break
        index += 1
    combo.remove(a)
    combo.remove(b)
    return combo[0]


def main():
    assert block_player(0, 3) == 6
    assert block_player(0, 8) == 4
    assert block_player(4, 8) == 0
    assert block_player(2, 5) == 8
    assert block_player(1, 7) == 4
    assert block_player(0, 4) == 8
    assert block_player(3, 5) == 4


if __name__ == '__main__':
    main()
