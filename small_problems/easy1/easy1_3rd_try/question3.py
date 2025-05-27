# Write another function that returns True if the string passed as an argument is a palindrome,
#  or False otherwise. This time, however, your function should be case-insensitive, and should 
# ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the is_palindrome 
# function you wrote in the previous exercise.

from question2 import is_palindrome

def clean_word(string):
    new_word = ''

    for char in string.casefold():
        if char.isalnum():
            new_word += char

    return new_word

def is_real_palindrome(string):
    cleaned_word = clean_word(string)

    return is_palindrome(cleaned_word)

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# practiced importing. 3:11 mins. easy use of creating a cleaned word where we don't need to worry 
# about word separation. easy use of alnum() method
