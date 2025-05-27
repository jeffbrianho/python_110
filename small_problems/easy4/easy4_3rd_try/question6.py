# Write a function that takes a string argument and returns a list of substrings of that string.
#  Each substring should begin with the first letter of the word, and the list should be ordered 
# from shortest to longest.

"""
I string
O: list of substrings
e: start with first substring letter and increment 0:1 0:2 0:3 etc
only strings

E: got it

D range for indices, list contructor comprehension

a: take a string, use lenrange to get increments
use slicing to get 0-1 0-2 etc. 

use list comprehension to make list in the range. return substring in comprehension

"""

def leading_substrings(string):
    return [string[:end + 1] for end in range(len(string))]



# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])