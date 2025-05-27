# Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.
"""
create reference list
use length to help with mulitple and add to list 
if 4 in length. use 1000 * number

"""
def string_to_integer(string):
    NUM_LIST =['0', '1', '2', '3', '4', 
                '5', '6', '7', '8', '9']

    final_num = 0

    lst_of_num = [(NUM_LIST.index(char)) for char in string]
    
    exponent = len(lst_of_num) - 1

    for num in lst_of_num:
        final_num += num * 10 ** exponent
        exponent -= 1
    
    return final_num


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

# 8:52 mins took some time with maths but got it in the end. good use of terminal for math
# they used the dictionary to pull the num - 