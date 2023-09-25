count_vowel = 0
count_char = 0
vowels = ['a', 'e', 'i', 'o', 'u']

strings = input("Name: ")

for string in strings:
    if string in vowels:
        count_vowel += 1
    count_char += 1

print(f"Out of {count_char} letters, {strings} has {count_vowel} vowels")