# The following dictionary has list values that contains strings. Write some code to 
# create a list of every vowel (a, e, i, o, u) that 
# appears in the contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

"""
O: List of vowel ['e']
A: get value of each item in dict giving a list with strings,
iterate through each object and append if char in list of values
append to list return list

"""
VOWELS = ('aeiouAEIOU')

# list_of_vowels = []
# for value in dict1.values():
#     for word in value:
#         for char in word:
#             if char in VOWELS:
#                 list_of_vowels.append(char)


list_of_vowels = [char for value in dict1.values()
                  for word in value
                  for char in word
                  if char in VOWELS]

print(list_of_vowels == ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o'])

#Their answer; can access more direct using key access
vowels = 'aeiou'

chars = [char for key in dict1
              for word in dict1[key]
              for char in word if char in vowels]

print(chars)