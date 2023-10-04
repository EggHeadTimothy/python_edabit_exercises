"""
Advanced List Sort by Timothy Eden
Date Last Modified: October 4, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/6vSZmN66xhMRDX8YT
"""


def advanced_sort(lst):
    """
    We first create a list that contains the unique values from the original list, then we create a sublist for each
    unique item containing the number of instances of that item in the original list.
    """
    result = []
    unique_items = []
    for thing in lst:
        if thing not in unique_items:
            unique_items.append(thing)
    for thing in unique_items:
        result.append([thing] * lst.count(thing))
    return result


def main():
    assert advanced_sort([1, 2, 1, 2]) == [[1, 1], [2, 2]]
    assert advanced_sort([2, 1, 2, 1]) == [[2, 2], [1, 1]]
    assert advanced_sort([3, 2, 1, 3, 2, 1]) == [[3, 3], [2, 2], [1, 1]]
    assert advanced_sort([5, 5, 4, 3, 4, 4]) == [[5, 5], [4, 4, 4], [3]]
    assert advanced_sort([80, 80, 4, 60, 60, 3]) == [[80, 80], [4], [60, 60], [3]]
    assert advanced_sort(['c', 'c', 'b', 'c', 'b', 1, 1]) == [['c', 'c', 'c'], ['b', 'b'], [1, 1]]
    assert advanced_sort([1234, 1235, 1234, 1235, 1236, 1235]) == [[1234, 1234], [1235, 1235, 1235], [1236]]
    assert advanced_sort(['1234', '1235', '1234', '1235', '1236', '1235']) == \
           [['1234', '1234'], ['1235', '1235', '1235'], ['1236']]


if __name__ == '__main__':
    main()
