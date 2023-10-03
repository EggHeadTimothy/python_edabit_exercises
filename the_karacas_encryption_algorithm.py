"""
The Karaca's Encryption Algorithm by Timothy Eden
Date Last Modified: October 3, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/JzBLDzrcGCzDjkk5n
"""


def encrypt(word):
    rev_word = word[::-1]
    output = ''
    for char in rev_word:
        if char == 'a':
            output += '0'
        elif char == 'e':
            output += '1'
        elif char == 'i':
            output += '2'
        elif char == 'o':
            output += '2'
        elif char == 'u':
            output += '3'
        else:
            output += char
    output += 'aca'
    return output


def main():
    assert encrypt("karaca") == "0c0r0kaca"
    assert encrypt("burak") == "k0r3baca"
    assert encrypt("banana") == "0n0n0baca"
    assert encrypt("alpaca") == "0c0pl0aca"
    assert encrypt("hello") == "2ll1haca"


if __name__ == '__main__':
    main()
