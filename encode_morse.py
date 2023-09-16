"""
Encode Morse by Timothy Eden
Date Last Modified: September 16, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/5bYXQfpyoithnQisa
"""

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}


def encode_morse(message):
    """
    Since the conversion to morse code does not differentiate between uppercase and lowercase letters, we first convert
    the message to all-uppercase. An empty string is then created which will contain the morse code. The index variable
    is created to track the index of the current character being iterated over, and another variable is created for the
    final index (this is because for the final character, a space is not added). Now, for each character in the message,
    the morse code equivalent is added to the morse string, and if we're not at the final index, a space is also added.
    """
    message = message.upper()
    morse = ''
    index = 0
    final_index = len(message) - 1
    for character in message:
        if index != final_index:
            morse += char_to_dots[character]
            morse += ' '
        else:
            morse += char_to_dots[character]
        index += 1
    return morse


def main():
    assert encode_morse("EDABBIT CHALLENGE") == ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
    assert encode_morse("HELP ME !") == ".... . .-.. .--.   -- .   -.-.--"
    assert encode_morse("CHALLENGE") == "-.-. .... .- .-.. .-.. . -. --. ."


if __name__ == '__main__':
    main()
