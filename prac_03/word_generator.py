"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABET = CONSONANTS + VOWELS

word_format = "%re#tly"
word = ""
for char in word_format:
    if char == "#":
        word += random.choice(VOWELS)
    elif char == "%":
        word += random.choice(CONSONANTS)
    elif char == "*":
        word += random.choice(ALPHABET)
    else:
        word += char

print(word)
