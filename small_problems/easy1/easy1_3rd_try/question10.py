# after reading how they did it with divmod and tuple reassignment

def integer_to_string(num):

    STRING_LIST = ['0', '1', '2', '3', '4', '5',
                    '6', '7', '8', '9']
    
    final_string = ''
    
    while num > 0:
        num, remainder = divmod(num, 10) # (432, 1)
        final_string = STRING_LIST[remainder] + final_string

    return final_string or '0'



print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True


# In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. In this exercise and the next, you're going to reverse those functions.

# Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

# You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

"""
create string list for reference and call the number
do same as last time for number length now can % 10 to get remaining numbers
number // 10 
add to final string, and reverse final string?

"""


def integer_to_string(num):
    STRING_LIST = ['0', '1', '2', '3', '4', '5',
                    '6', '7', '8', '9']

    final_rev_string = ''

    if num == 0:
        return '0'

    while num > 0:
        tuple_num = divmod(num, 10)
        final_rev_string += STRING_LIST[tuple_num[1]]
        num = tuple_num[0]
    
    
    return final_rev_string[::-1]
    
    

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# without the divmod function, 10:04 seconds