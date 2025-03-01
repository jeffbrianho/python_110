# Write a function that takes a list of strings and returns a list of the same string values, 
# but with all vowels (a, e, i, o, u) removed.

"""
i: list of strings
o: same list of string with all vowels removed

e: multiple elements, same order, empty strings caps or lower

i
E 
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected) 

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ'] return an empty string

D: list, strings
A
make final list/array
iterate through original list
have empty placeholder string
iterate through each char and return to placeholder if != vowel
append final string to list
return final list

"""
VOWELS = 'aeiouAEIOU'

def remove_vowels(lst):
   
    final_lst = [''.join([char for char in string
                        if char not in VOWELS])
                        for string in lst]
    
    return (final_lst)

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

#Their answer
def strip_vowels(string):
    VOWELS = "aeiouAEIOU"
    no_vowels = [char for char in string
                 if char not in VOWELS]
    return ''.join(no_vowels)

def remove_vowels(string_list):
    return [strip_vowels(string) for string in string_list]

#MAKE TWO FUNCTIONS  cleaner!