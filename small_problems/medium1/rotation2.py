# Write a function that rotates the last count digits of a number. 
# To perform the rotation, move the first of the digits that you want 
# to rotate to the end and shift the remaining digits to the left.

"""
P
I: integer
O: integer
E: have a decimal place and move the number in that place to the end, push the others to the left
I

E
D: string?
A:
Use a string to manipulate digits?
convert to string
use negative indexing to access the correct char
remove char and concatenate to end
convert to int

"""

def rotate_rightmost_digits(num, place):
    string_num = str(num)
    if place == 1:
        return num 
    else:
        new_string = string_num[:-place] + string_num[-place + 1:] + string_num[-place]
        return int(new_string)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True



# Their answer:
# split the num beteween untouched and rotating. function to rotate, then concatenate.

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)

def rotate_string(string):
    return string[1:] + string[0]

#This will edit a digit from the indicated place to the end while maintaining all the other numbers
# Their answer

def rotate_rightmost_digits(number, count):
    number_str = str(number)
    first_part = number_str[:-count]
    second_part = number_str[-count:]
    result_str = first_part + rotate_string(second_part)

    return int(result_str)

def rotate_string(string):
    return string[1:] + string[0]