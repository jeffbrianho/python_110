# Write a function that takes a string as input and counts the occurrences of each
# lowercase letter in the string. Return the counts in a dictionary where the
# letters are keys and their counts are values.

"""
A set method for letters then count compared to string

"""
def letter_count(string):
    return {char: string.count(char) for char in set(string)}

print(letter_count('launchschool') == { 'a': 1, 'c': 2, 'h': 2, 'l': 2, 'o': 2, 'u': 1, 's': 1, 'n': 1})

