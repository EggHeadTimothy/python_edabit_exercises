"""
Prison Break by Timothy Eden
Date Last Modified: October 4, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/SHdu4GwBQehhDm4xT
"""


def switch_locks(prison):
    new_prison = []
    for cell in prison:
        if cell == 0:
            new_prison.append(1)
        elif cell == 1:
            new_prison.append(0)
    return new_prison


def freed_prisoners(prison):
    """
    Assuming the first cell isn't locked, we check each cell to see if it's a 0 or 1. If it's a 1, we increment the
    accumulator tracking the number of prisoners freed, and use our helper function to switch the locks. At the end, we
    return the accumulator.
    """
    if prison[0] == 0:
        return 0

    freed = 0

    for i in range(len(prison)):
        cell = prison[i]
        if cell == 1:
            freed += 1
            prison = switch_locks(prison)
        elif cell == 0:
            pass

    return freed


"""
Alternate solution found on Edabit:

return sum([1 if prison[i] != prison[i-1] else 0 for i in range(1, len(prison))]) + 1 if prison[0] == 1 else 0
"""


def main():
    assert freed_prisoners([1, 1, 0, 0, 0, 1, 0]) == 4
    assert freed_prisoners([1, 0, 0, 0, 0, 0, 0]) == 2
    assert freed_prisoners([1, 1, 1, 0, 0, 0]) == 2
    assert freed_prisoners([1, 0, 1, 0, 1, 0]) == 6
    assert freed_prisoners([1, 1, 1]) == 1
    assert freed_prisoners([0, 0, 0]) == 0
    assert freed_prisoners([0, 1, 1, 1]) == 0


if __name__ == '__main__':
    main()
