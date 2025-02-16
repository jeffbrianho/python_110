# Write another function that returns True if the string passed as an argument is a palindrome, 
# or False otherwise. This time, however, your function should be case-insensitive, and should 
# ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the
# is_palindrome function you wrote in the previous exercise.

from palindrome import is_palindrome


def is_real_palindrome(s):
    clean_s = ''
    for char in s:
        if char.isalnum():
            clean_s += char.casefold()
    return is_palindrome(clean_s)

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True