"""
Longest Word by Timothy Eden
Date Last Modified: June 27, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/Aw2QK8vHY7Xk8Keto
"""


def longest_word(s):
    result = ''
    all_words = []
    current_word = ''
    for letter in s:
        if letter != ' ':
            current_word += letter
        if letter == ' ' or letter == s[-1]:
            all_words.append(current_word)
            current_word = ''
    for word in all_words:
        if len(word) > len(result):
            result = word
    return result


def main():
    assert longest_word("Margaret's toy is a pretty doll.") == "Margaret's"
    assert longest_word("A thing of beauty is a joy forever.") == "forever."
    assert longest_word("Forgetfulness is by all means powerless!") == "Forgetfulness"


if __name__ == '__main__':
    main()
