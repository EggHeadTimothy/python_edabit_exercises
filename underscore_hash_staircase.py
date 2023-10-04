"""
Underscore-Hash Staircase by Timothy Eden
Date Last Modified: October 4, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/YqLBEZJR9ySndYQpH
"""


def staircase(n):
    """
    If n is positive, the number of underscores starts as (n - 1) and decrements each time, and if n is negative, the
    number of underscores starts at 0 and increments each time. The variable underscores keeps track of how many
    underscores are needed on each line, so that number of underscores is printed, then the remainder of the line is
    filled with hashes.
    """
    staircase = ''
    underscores = 0
    if n > 0:
        underscores = n - 1
    nabs = abs(n)
    for i in range(nabs):
        for _ in range(underscores):
            staircase += '_'
        for _ in range(nabs - underscores):
            staircase += '#'
        if (i + 1) != nabs:
            staircase += '\n'
            if n > 0:
                underscores -= 1
            elif n < 0:
                underscores += 1
    return staircase


"""
Better solution found:

return '\n'.join(['_' * (abs(n) - 1 - i) + '#' * (i + 1) for i in range(abs(n))][::n // abs(n)])
"""


def main():
    assert staircase(3) == "__#\n_##\n###"
    assert staircase(7) == "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
    assert staircase(2) == "_#\n##"
    assert staircase(-8) == "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"


if __name__ == '__main__':
    main()
