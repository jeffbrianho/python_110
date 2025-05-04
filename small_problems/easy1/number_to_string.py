# In the previous two exercises, you developed functions that convert simple numeric strings
#  to signed integers. In this exercise and the next, you're going to reverse those functions.

# Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to
#  the string representation of that integer.

# You may not use any of the standard conversion functions available in Python, such as str.
#  Your function should do this the old-fashioned way and construct the string by analyzing 
# and manipulating the number.

"""
P:
I: integer
O: string representation
E: no functions. analyze and manipulate the number
I

E:
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

D: string; placeholder 
dict for comparison

A
determine the letter type and add to final string in place

"""

def integer_to_string(num):
    DIGITS = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        0: '0',

    }
    final_string = ''
    
  
    if num == 0:
        return "0"
    
    while num > 0:
        single_num = (num % 10)
        final_string += DIGITS[single_num]
        num //= 10
  
    return final_string[::-1]

"""
take num and len of num % 10
"""

# Theirs

# DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# def integer_to_string(number):
#     result = ''

#     while number > 0:
#         number, remainder = divmod(number, 10)
#         result = DIGITS[remainder] + result

#     return result or '0'
# USE THE INDEX TO ACCESS THE LIST: INTEGER INDEXING

# print(integer_to_string(4321) == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
# print(integer_to_string(1234567890) == "1234567890")  # True

"""
P
I: int
O: str
E
I

E
D: list or dict?
will need to reference each number to corresponding string num

A:
get number to individual digit by dividing. 
store each digit into a list?
iterate through each and compare to reference list/dict and return corresponding string

how to get first number? numb % will get last numb and // will cut the number short!

"""

def break_num_list(num):
    storage_list = []

    if num == 0:
        return [0]
    
    else:

        while num:
            storage_list.append(num % 10)
            num = num // 10

    return storage_list[::-1]

def integer_to_string(num):
    final_string = ''

    REFERENCE = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
    }

    num_list = break_num_list(num)

    for dig in num_list:
        final_string += REFERENCE[dig]
    
    return final_string
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# 10 mins or so
