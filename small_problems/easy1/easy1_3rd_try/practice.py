#  Write a function that takes a string of digits and returns the appropriate number as an integer. 
# You may not use any of the standard conversion functions available in Python, such as int. 
# Your function should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry about invalid 
# characters; assume all characters are numeric.

def string_to_integer(str_num):
    
    NUM_DICT = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '0': 0,
    }
    final_num = 0
    for char in str_num:
        final_num = (10 * final_num) + NUM_DICT[char]
    
    return final_num

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True