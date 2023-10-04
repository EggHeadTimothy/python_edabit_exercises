"""
Vowel Families by Timothy Eden
Date Last Modified: October 4, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/uwFHSRewNpmBNvbME
"""


def same_vowel_group(w):
    """
    Based on the first word, we must create a list of bad vowels (vowels not contained in the first word) and good
    vowels (vowels contained in the first word). For a word to become part of the result, it must contain NONE of the
    bad vowels, and ALL of the good vowels. If any of this is not true, the variable flag becomes False and the word
    is not added to the result.
    """
    result = []
    bad = ['a', 'e', 'i', 'o', 'u']
    good = []
    first = w[0]
    result.append(first)
    del w[0]
    for letter in first:
        if letter in 'aeiou' and letter not in good:
            good.append(letter)
            bad.remove(letter)
    for word in w:
        flag = True
        for letter in word:
            if letter in bad:
                flag = False
        if flag:
            for letter in good:
                if letter not in word:
                    flag = False
        if flag:
            result.append(word)
    return result


"""
Better solution found:

return [word for word in w if set(letter for letter in word if letter in 'aeiou') == 
set(letter for letter in w[0] if letter in 'aeiou')]
"""


def main():
    assert same_vowel_group(["hoops", "chuff", "bot", "bottom"]) == ["hoops", "bot", "bottom"]
    assert same_vowel_group(["crop", "nomnom", "bolo", "yodeller"]) == ["crop", "nomnom", "bolo"]
    assert same_vowel_group(["semantic", "aimless", "beautiful", "meatless icecream"]) == \
           ["semantic", "aimless", "meatless icecream"]
    assert same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) == ["many"]
    assert same_vowel_group(["toe", "ocelot", "maniac"]) == ["toe", "ocelot"]
    assert same_vowel_group(["a", "apple", "flat", "map", "shark"]) == ["a", "flat", "map", "shark"]
    assert same_vowel_group(["a", "aa", "ab", "abc", "aaac", "abe"]) == ["a", "aa", "ab", "abc", "aaac"]


if __name__ == '__main__':
    main()
