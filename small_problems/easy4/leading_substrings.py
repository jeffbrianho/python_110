# Write a function that takes a string argument and returns a list of substrings of that string.
#  Each substring should begin with the first letter of the word, 
# and the list should be ordered from shortest to longest.


"""
I: string
O: list of substrings
E: first letter of word, shortest to longest. 


iterate through string, append each to two things one saved string one to list or


for char in string: 
    final_char += char
    append final char

iterate through using slicing increasing the size of the slice through each iteration. 
0:1 0:2, 0:3 (range of length of string?)

THEIR ANSWER
def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

"""

def leading_substrings(s):
    final_lst = []
    growing_char = ''

    for char in s:
        growing_char += char
        final_lst.append(growing_char)

    return final_lst



# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

#This will provide a list of substrings from the leading letter and concatenating the next for each element

# 3 mins
def leading_substrings(string):
    return [string[:end + 1] for end in range(len(string))]