# A pangram is a sentence that contains every single letter of the alphabet at
# least once. Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not. Ignore numbers and punctuation.

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def is_panagram(sentence):
   return all([char in set(sentence) for char in set(ALPHABET)])

# Examples:
print(is_panagram("The quick brown fox jumps over the lazy dog.")) # == True)
print(is_panagram("This is not a pangram.") == False)