"""
Atbash Cipher by Timothy Eden
Date Last Modified: October 3, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/MGALfBAXhXqqdFyqo
"""


mirror = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P',
          'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E',
          'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A', 'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't',
          'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
          's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}


def atbash(txt):
    """
    The dictionary mirror contains every letter of the alphabet in uppercase and lowercase as keys, and each key has its
    mirror letter as its value. We begin with result as an empty string, and iterate through each character of txt. If
    the character is not in the mirror dictionary, we simply add it to the result string unaltered. Otherwise, we use
    the dictionary to add its mirror equivalent.
    """
    result = ''
    for char in txt:
        if char not in mirror:
            result += char
        else:
            result += mirror[char]
    return result


def main():
    assert atbash("abcdefghijklmnopqrstuvwxyz") == "zyxwvutsrqponmlkjihgfedcba"
    assert atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    assert atbash("The word 'atbash' derives from the the first and last 2 letters of the Hebrew alphabet.") ==\
        "Gsv dliw 'zgyzhs' wvirevh uiln gsv gsv urihg zmw ozhg 2 ovggvih lu gsv Svyivd zokszyvg."
    assert atbash("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi.") ==\
           "Encryption and decryption are identical for the Atbash cipher."


if __name__ == '__main__':
    main()
