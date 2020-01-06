from string import ascii_letters
import random


def generate_id():
    return ''.join(random.choice(ascii_letters) for i in range(3))


def decrypt(text, s=5):
    result = ""
    letters = ascii_letters

    for char in text:
        if char in letters:
            char_index = (letters.find(char) - s) % len(letters)
            result += letters[char_index]
        else:
            result += char
    return result


def encrypt(text, s=5):
    result = ""
    letters = ascii_letters

    for char in text:
        if char in letters:
            char_index = (letters.find(char) + s) % len(letters)
            result += letters[char_index]
        else:
            result += char
    return result