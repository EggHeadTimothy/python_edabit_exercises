"""
Playing RisiKo! by Timothy Eden
Date Last Modified: September 24, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/TY2mJcZR8LBWepu7T
"""


def risiko(attacker, defender):
    """
    The variable how_many determines how many comparisons will be done (equal to the length of the shortest list, which
    means the player who rolled the least dice). This is initialized as 3 (the maximum possible value), then the length
    of each list is compared to how_many to determine if the value needs to be lowered. Afterwards, since the dice are
    compared starting with the highest value, we must sort the lists from highest to lowest. Then, for the number of
    times determined using how_many, each dice in the attacker list is compared to the dice of the same index in the
    defender list, and if the attacker has a higher number, the accumulator variable def_lost is incremented by 1
    (tracking the amount of armies lost by the defender).
    """
    def_lost = 0
    how_many = 3
    for i in [len(attacker), len(defender)]:
        if i < how_many:
            how_many = i
    attacker.sort(reverse=True)  # sorts from highest to lowest
    defender.sort(reverse=True)
    for i in range(how_many):
        if attacker[i] > defender[i]:
            def_lost += 1
    return def_lost


def main():
    assert risiko([3, 6, 4], [2, 5, 3]) == 3
    assert risiko([3, 6], [6, 4, 4]) == 0
    assert risiko([3, 1], [1]) == 1
    assert risiko([4, 4, 3], [3, 2]) == 2
    assert risiko([5], [3, 1, 4]) == 1
    assert risiko([3, 5], [3, 5]) == 0
    assert risiko([3, 6, 6], [6]) == 0
    assert risiko([5, 4], [3, 4, 3]) == 2
    assert risiko([3], [2, 1]) == 1
    assert risiko([3, 3, 3], [2, 1, 2]) == 3


if __name__ == '__main__':
    main()
