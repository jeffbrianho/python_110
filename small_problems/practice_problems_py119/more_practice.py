#  ​Basic​: Create a function called count_vowels that takes a string as an argument and returns the number of vowels (a, e, i, o, u) in the string, regardless of case.

"""
I: string
O: integer
e: number of vowels in the string, regardless of case
I: y is not a vowel case does not matter

E 
1. e, o
2. o


D: consider list of vowels? return len?
can use a simple counter when iterating

A:

can do a iteration through the string and count if the char is in a storage of vowesl; can store the case or just
casefold()

create a reference vowel list
itertate through string and append to list if in vowel
    - when iterating use casefold. 
return the len of that list

"""

# def count_vowels(string):
    
#     VOWELS = 'aeiou'

#     return len([vowel for vowel in string.casefold()
#                     if vowel in VOWELS])

# # Examples
# print(count_vowels("hello") == 2)
# print(count_vowels("Python") == 1)
# print(count_vowels("aeiou") == 5)
# print(count_vowels("AEIOU") == 5)
# print(count_vowels("bcdfghjklmnpqrstvwxyz") == 0)

# ​Intermediate​: Create a function called palindrome_substrings that takes a string as an argument and returns a list of all palindromic substrings with a length greater than 1.
"""
I: string
O: list of substrings
E: palindromic substring length greater than 1
I:

E: wrong cause bb and ll is not in the list so greater than 2 will meet the demands

D: list of all substrings if len> 1

A:
create a substring from index (range length) "i" start counter  - range (length of string) + 1 `j` end counter
append the word if that string == [::-1 ] and len > 2 or greater than 1
return the list. 

"""
# def palindrome_substrings(string):
#     return [string[i:j] for i in range(len(string))
#                 for j in range(i + 1, len(string) + 1)
#                 if string[i:j] == string[i:j][::-1] and len(string[i:j]) > 2]
# # Examples
# print(sorted(palindrome_substrings("abba")) == ["abba"])
# print(sorted(palindrome_substrings("abbac")) == ["abba"])
# print(sorted(palindrome_substrings("racecar")) == ["aceca", "cec", "racecar"])
# print(sorted(palindrome_substrings("hello")) == [])
    

# Intermediate​: Create a function called most_frequent_char that takes a string as an argument and returns the most frequently occurring character. If there's a tie, return the character that appears first in the string.
    

""""
P
I: STRING
O: char string
E: most frequently occuring char
I: all lowercase
no string == no string


D: can do a count and return max count?
create a dictionary and return max value, I think max returns the first occurence

D

A
:
if string:
create a dictionary/count
create key that returns dictionar[key] `value`
return max value with key=key - will the max give the first occurence?
if not iterate through word and if char == max count return char
"can reverse iterate to get last , try that next"


# """
# def most_frequent_char(string):
#     if string:
#         char_dict = {char: string.count(char) for char in string}
        
#         def key_value(key):
#             return char_dict[key]
        
#         max_count = max(char_dict.values())

#         print(max_count)
#         for char in string[::-1]:
#             if string.count(char) == max_count:
#                 return char
#     else:
#         return string
# # Examples
# print(most_frequent_char("hello") == "l")
# print(most_frequent_char("abcdefg") == "g")
# print(most_frequent_char("mississippi") == "i")
# print(most_frequent_char("") == "")


#  ​Advanced​: Create a function called convert_to_title that takes a string and converts it to title case according to specific rules: the first word and any word after a period, colon, or dash should be capitalized, as well as important words. Words like "a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to", "from", "by", "with" should not be capitalized unless they're the first word in the title.


"""
I: string
O: string
E: output is string converted to title case if
    - first word
        - any word after a period, colon, or dash
        - a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to", "from", "by", "with"  not
I

E

Dlist of words:


A:
create a list of words
if wordlist is [0] then capitalize

    if word[-1][-1] in wordlist in(criteria) 
    come back to check to see if able to get last char in previous word, careful with index error
    append capital

else ; if word not in list capitialize

"""

# def convert_to_title(string):
#     word_list = string.split()

#     BAD_WORDS = ["a", "an", "the", "and", "but", "or", "for", "nor", "on", "at", "to", "from", "by", "with", "of"]
#     PUNT = '.:-'

#     title_list = []
    
#     for index, word in enumerate(word_list):
#         if index == 0:
#             title_list.append(word.title())
#         elif word_list[index - 1][-1] in PUNT:
#             title_list.append(word.title())
#         elif word not in BAD_WORDS:
# #             title_list.append(word.title())
# #         else:
# #             title_list.append(word)
# #     return ' '.join(title_list)




# # # Examples
# # print(convert_to_title("the lord of the rings") == "The Lord of the Rings")
# # print(convert_to_title("a tale of two cities") == "A Tale of Two Cities")
# # print(convert_to_title("to kill a mockingbird") == "To Kill a Mockingbird")


# def bubble_sort(lst):
#     while True:
#         swapped = False
#         for indx in range(1, len(lst)):
#             if lst[indx -1] < lst[indx]:
#                 continue

#             lst[indx - 1], lst[indx] = lst[indx], lst[indx - 1]
#             swapped = True

#         if not swapped:
#             break

# lst1 = [5, 3]
# bubble_sort(lst1)
# print(lst1 == [3, 5])                   # True

# lst2 = [6, 2, 7, 1, 4]
# bubble_sort(lst2)
# print(lst2 == [1, 2, 4, 6, 7])          # True

# lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#         'Kim', 'Bonnie']
# bubble_sort(lst3)

# expected = ["Alice", "Bonnie", "Kim", "Pete",
#             "Rachel", "Sue", "Tyler"]
# print(lst3 == expected)                 # True



#   ​Intermediate​: Create a function called run_length_encode that implements a simple form of run-length encoding. For consecutive repeating characters, replace them with the character followed by the count. If a character doesn't repeat, just leave it as is.'

"""
P
I: string
O: string
Eif consecutive replace them with the char vs count
if not consecutive leave as is 
Ino string == string

E

D: function to `count` and return number as string


A:

iterate through string if char = next char start count
continue until char != char and concatenate count to string as charcount reset char to 1
if count != 1 concatenate char


"""

# def run_length_encode(string):
#     final_string = ''

#     count = 1
#     for indx in range(1, len(string)):  #0 ,1, 2, 3, 4
#         if string[indx] == string[indx - 1]:
#             count += 1
#         elif string[indx] != string[indx - 1] and count != 1:
#             final_string += f'{string[indx - 1]}{count}'
#             count = 1
#         else:
#             final_string += string[indx - 1]

#         if count != 1 and indx == len(string) - 1:
#             final_string += f'{string[indx]}{count}'
#         elif count == 1 and indx == len(string) - 1:
#             final_string += string[indx]

#     return final_string

# # Examples
# print(run_length_encode("aabccc") == "a2bc3")
# print(run_length_encode("wwwwaaadexxxxxx") == "w4a3dex6")
# print(run_length_encode("abc") == "abc")
# print(run_length_encode("") == "")
    

# Advanced​: Create a function called find_anagrams that takes two arguments: a list of strings and a target string. Return a list of all strings from the list that are anagrams of the target string.


# def find_anagrams(words, target):

#     def create_dict(string):
#         return {char: string.count(char) for char in string}
    
#     return [word for word in words
#             if create_dict(word) == create_dict(target)]

# Examples
# print(sorted(find_anagrams(["listen", "silent", "enlist", "hello"], "listen")) == ["enlist", "listen", "silent"])
# print(sorted(find_anagrams(["act", "cat", "dog", "tac"], "cat")) == ["act", "cat", "tac"])
# print(find_anagrams(["python", "java", "ruby"], "javascript") == [])
    

# ​Intermediate​: Create a function called longest_common_prefix that takes a list of strings and returns the longest common prefix string among them.

"""
list of strings
longest common prefix

create substrings of prefixes if prefix in all append to list return lonigest string 
can iterate all indices and if beginning is the same append until it is not,
return the final string


"""

# def longest_common_prefix(strings=''):
    
#     final_string = ''
    
#     if strings:

#         shortest_word = min(strings, key=len)

#         for index in range(len(shortest_word)):
#             if all([strings[w_index][index] == strings[w_index - 1][index]
#                     for w_index in range(1, len(strings))]):
#                     final_string += strings[0][index]

#     return final_string

# # Examples
# print(longest_common_prefix(["flower", "flow", "flight"]) == "fl")
# print(longest_common_prefix(["dog", "racecar", "car"]) == "")
# print(longest_common_prefix(["python", "pypy", "py"]) == "py")
# print(longest_common_prefix([]) == "")
    

# ​Advanced​: Create a function called word_pattern that takes two string arguments: a pattern and a string of space-separated words. Return True if there is a one-to-one correspondence between a pattern letter and a word.

"""
2 strings
pattern correspondence

use a mapping?
assign each char to the letter

dict.setdefault(char, word[0])
compare if dict == dict return true
set definitionts
for dictionar[key(index)] == list[index] 
"""

# def word_pattern(pattern, string):
#     pattern_list = list(pattern)
#     string_list = string.split()

#     short_list = []
#     for word in string_list:
#         if word not in short_list:
#             short_list.append(word)

#     short_pattern =[]
#     for char in pattern_list:
#         if char not in short_pattern:
#             short_pattern.append(char)
    
#     if len(short_pattern) == len(short_list):

#         KEY_DICT = {}
#         for index in range(len(short_pattern)):
#             KEY_DICT.setdefault(short_pattern[index], short_list[index]) 
        
    
#         return all(([KEY_DICT[pattern_list[index]] == string_list[index] for index in range(len(string_list))]))
#     else:
#         return False


# Examples
# print(word_pattern("abba", "dog cat cat dog") == True)
# print(word_pattern("abba", "dog cat dog cat") == False)
# print(word_pattern("aaaa", "dog dog dog dog") == True)
# print(word_pattern("abba", "dog dog dog dog") == False)
    
#   ​Advanced​: Create a function called compress_string that takes a string and compresses it using the following algorithm: for each group of consecutive repeating characters, replace the group with the character followed by the count (in brackets). If a character doesn't repeat, just leave it as is.



# def compress_string(string):
#     final_string = ''

#     if string:
#         char_dict = {char: string.count(char) for char in string}

    

#         for char_key, count in char_dict.items():
#             if count > 1:
#                 final_string += f'{char_key}[{count}]'
#             else:
#                 final_string += char_key
        
#     return final_string

# # Examples
# print(compress_string("aabccc") == "a[2]bc[3]")
# print(compress_string("wwwwaaadexxxxxx") == "w[4]a[3]dex[6]")
# print(compress_string("abc") == "abc")
# print(compress_string("") == "")



# ​Advanced​: Create a function called string_expansion that takes a string like "3a2bc4d" and expands it to "aaabcdddd". If there is no number before a letter, it is expanded once.

"""

run through each string if string.isnumeric
append next one to string times int(char)
if not append
"""



def string_expansion(string):
    final_string = ''

    if string:
        for index in range(len(string)):
            if string[index].isnumeric():
                final_string += string[index + 1] * (int(string[index]) - 1)
            else:
                final_string += string[index]
    
    return final_string
# Examples
print(string_expansion("3a2bc4d") == "aaabbcdddd")
print(string_expansion("3d2a") == "dddaa")
print(string_expansion("3abc") == "aaabc")
print(string_expansion("abcd") == "abcd")
print(string_expansion("") == "")