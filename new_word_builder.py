"""
New Word Builder by Timothy Eden
Date Last Modified: June 27, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/R5F99DeuhqYxbGyMM
"""


def word_builder(ltr, pos):
    result = ''
    for i in pos:
        result += ltr[i]
    return result


def main():
    assert word_builder(["g", "e", "o"], [1, 0, 2]) == 'ego'
    assert word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) == 'test'
    assert word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]) == 'edabit'
    assert word_builder(["l", "e", "h", "n", "l", "c", "a", "e", "g"], [5, 2, 6, 4, 0, 1, 3, 8, 7]) == 'challenge'
    assert word_builder(["s", "o", "r", "t", "e", "d"], [0, 1, 2, 3, 4, 5]) == 'sorted'


if __name__ == '__main__':
    main()
