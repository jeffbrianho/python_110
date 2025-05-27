# In the previous exercise, you developed a function that converts simple numeric strings to 
# integers. In this exercise, you're going to extend that function to work with signed numbers.

# Write a function that takes a string of digits and returns the appropriate number as an integer.
#  The string may have a leading + or - sign; if the first character is a +, your function should 
# return a positive number; if it is a -, your function should return a negative number. 
# If there is no sign, return a positive number.

# You may assume the string will always contain a valid number.

# You may not use any of the standard conversion functions available in Python, such as int.
#  You may, however, use the string_to_integer function from the previous exercise.

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


def string_to_signed_integer(string):
    cleaned_string = ''
    for char in string:
        if char.isdigit():
            cleaned_string += char
        
    if string.startswith('-'):
        return string_to_integer(cleaned_string) * -1
    else:
        return string_to_integer(cleaned_string)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

# 2:59 mins. had to account for nondigit with calculations. easy otherwise. 