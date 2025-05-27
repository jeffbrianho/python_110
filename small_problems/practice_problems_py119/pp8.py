# Create a function that takes a non-empty string as an argument. 
# The string consists entirely of lowercase alphabetic characters. 
# The function should return the length of the longest vowel substring.
#  The vowels of interest are "a", "e", "i", "o", and "u".

"""
P
I: string
O: len of longest vowel substring
E: length of longest cosecutive substring of vowels 
I

E: au for launch or oo
eau

D: list of substrings that are values

A:
iterate through string
    - char in string 
concatenate a vowel substring if char in vowels
    if char in vowels concatenate
    if not append to list and restart string

append to list if next is not:
create a length of substrings, return the max num

"""

def longest_vowel_substring(s):
    VOWELS = 'aeiou'
    substring_lst = []
    substring = ''

    for char in s:
        if char in VOWELS:
            substring += char
        else:
            substring_lst.append(substring)
            substring = ''
        substring_lst.append(substring)


    length_list = [len(subs) for subs in substring_lst]
    return max(length_list)



print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

# 9:56 mins forgot to append if the non-vowel condition was never met
