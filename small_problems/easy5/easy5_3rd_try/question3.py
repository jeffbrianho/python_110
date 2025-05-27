# Write a function that takes a list of strings and returns a list 
# of the same string values, but with all vowels (a, e, i, o, u) removed.

"""
I: list string
O list string
E string with all vowels removed
i: CAP sensitive

create vowels reference
iterate through each word
iterate through each char if char is in vowels skip

create word function.
for each char in word if != vowel
concatenate letter to string
return new string 

create iterator list function - 
return new word with function for each word in the list. 



"""
VOWELS = 'aeiou'

def no_vowel_word(word):
    new_string = ''
    for char in word:
        if char.casefold() not in VOWELS:
            new_string += char
    return new_string

def remove_vowels(lst_of_strings):
    return [no_vowel_word(word) for word in lst_of_strings]

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

# 6:10 mins
# did good with testing, need to check examples more 