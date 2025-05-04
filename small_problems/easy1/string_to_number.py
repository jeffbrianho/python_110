# Write a function that takes a string of digits and returns the appropriate number as an 
# integer. You may not use any of the standard conversion functions available in Python, 
# such as int. Your function should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry about invalid 
# characters; assume all characters are numeric.


"""
P:
INPUT: string of digits
OUTPUT: integer
EXPLICIT: take a string of digits and return the number: without using functions such as int assume all numeric
IMPLICIT

E:
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
D
A: determine the length of the number and for each place add a zero is necessary and start with string to number
sum all the integers and return the value.
make a counter from largest to end 

"""

def string_to_single_int(s):
    match s:
        case '1':
            return 1
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return 4
        case '5':
            return 5
        case '6':
            return 6
        case '7':
            return 7
        case '8':
            return 8
        case '9':
            return 9
        case '0':
            return 0


def string_to_integer(s):

    count = len(s)

    number = 0 

    for char in s:
        count -= 1
        number += string_to_single_int(char)* 10**count

    return (number)
        


#their answer

# def string_to_integer(s):
#     DIGITS = {
#         '0': 0,
#         '1': 1,
#         '2': 2,
#         '3': 3,
#         '4': 4,
#         '5': 5,
#         '6': 6,
#         '7': 7,
#         '8': 8,
#         '9': 9,
#     }

#     value = 0
#     for char in s:
#         value = (10 * value) + DIGITS[char]

#     return value
    

# print(string_to_integer("4321")  == 4321)  # True
# print(string_to_integer("570") == 570)    # True

def string_to_integer(string):
    LIST_OF_INT = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 

    num_list = [(LIST_OF_INT.index(num) * (10 ** (len(string) - (indx + 1)))) for indx, num in enumerate(string)]
    return sum(num_list)
        

print(string_to_integer("4321"))# == 4321)  # True
print(string_to_integer("570") == 570)    # True

# 8 mins