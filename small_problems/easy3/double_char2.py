# Write a function that takes a string, doubles every consonant in the string, and 
#  returns the result as a new string. The function should not double vowels ('a','e','i','o','u'),
#  digits, punctuation, or whitespace.

# You may assume that only ASCII characters will be included in the argument.


def double_consonants(s):
    final_s = ''
    for char in s:
        if char.casefold() in ('bcdfghjklmnpqrstvwxyz'):
            final_s += char * 2
        else:
            final_s += char
    return final_s

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")


def repeater(string):
    return ''.join([char * 2 for char in string])

def double_consonants(string):
    VOWELS = 'aeiouAEIOU'
    return ''.join([repeater(consonant) if consonant not in VOWELS and consonant.isalpha() 
                                        else consonant
                                        for consonant in string
                                        ])
