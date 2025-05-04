# Create a function that takes a non-empty string as an argument. 
# The string consists entirely of lowercase alphabetic characters. 
# The function should return the length of the longest vowel substring. 
# The vowels of interest are "a", "e", "i", "o", and "u".

"""
P
I:string
O: int
e: len of longest vowel substring
E
I must be consecutive

E
D: list of iterations
A: iterate through each char: if char is not vowel, go to next and continue to add


"""

def longest_vowel_substring(string):
    VOWELS = 'aeiou'

    list_of_substrings =[] 

    longest_vowel = ''
    for char in string:
        if char in VOWELS:
            longest_vowel += char
        else:
            list_of_substrings.append(longest_vowel)
            longest_vowel = ''
        list_of_substrings.append(longest_vowel)
    return max([len(substring) for substring in list_of_substrings])
    
print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)