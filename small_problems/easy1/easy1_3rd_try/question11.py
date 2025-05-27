# In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

# Write a function that takes an integer and converts it to a string representation.

# You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.



"""
if statement if 0
if >0
if < 0
append number to front of string? hard code?


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
    
def signed_integer_to_string(num):
    if num == 0:
        return integer_to_string(num)
    elif num > 0:
        return '+' + integer_to_string(num)
    else:
        return  '-' + integer_to_string(num * -1)

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

# 2 mins due to - symbol but worked well needed to adjust to positive 

# they used f stringing
