"""
Beginning and End Pairs by Timothy Eden
Date Last Modified: July 2, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/HrCuzAKE6skEYgDmf
"""


def pairs(lst):
    result = []
    lst_copy = lst.copy()
    while len(lst_copy) > 0:
        if len(lst_copy) == 1:
            pair = [lst_copy[0], lst_copy[0]]
            lst_copy.remove(lst_copy[0])
        else:
            pair = [lst_copy[0], lst_copy[-1]]
            del lst_copy[-1]
            del lst_copy[0]
        result.append(pair)
    return result


def main():
    assert pairs([1, 2, 3, 4, 5, 6, 7]) == [[1, 7], [2, 6], [3, 5], [4, 4]]
    assert pairs([1, 2, 3, 4, 5, 6]) == [[1, 6], [2, 5], [3, 4]]
    assert pairs([5, 9, 8, 1, 2]) == [[5, 2], [9, 1], [8, 8]]
    assert pairs([1, 1, 4, 4, 5, 5]) == [[1, 5], [1, 5], [4, 4]]
    assert pairs([9, 9, 9, 9, 3, 3, 9]) == [[9, 9], [9, 3], [9, 3], [9, 9]]
    assert pairs([5, 6, 7]) == [[5, 7], [6, 6]]
    assert pairs([5, 6]) == [[5, 6]]
    assert pairs([5]) == [[5, 5]]
    assert pairs([]) == []


if __name__ == '__main__':
    main()
