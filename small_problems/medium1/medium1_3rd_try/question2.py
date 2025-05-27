# Write a function that rotates the last count digits of a number. 
# To perform the rotation, move the first of the digits that you want to 
# rotate to the end and shift the remaining digits to the left.


"""
P
I: integer, integer at place
O: single rotated integer
E: shift all other numbers to left and replace at level indicated by number
I


E: 735291, 2 ==> 735219
    1200, 3 ==> 1002

D: strings to manipulate the integer

A:
change first number into a string:
    str(number)
use the second argument as negative index to achieve area to manipulate
    - [-indx + 1](element)
remove that digit and place at end of string
    - slice the number from [:-indx] beginning and [-indx](element) and [-indx + 1:] end
    - concatenate beginning + end + element
return string as an integer
    return int(string)

"""

def rotate_rightmost_digits(number, place):
    str_num = str(number)

    element = str_num[-place]
    beginning = str_num[:-place]
    end = str_num[-place + 1:]

    if place == 1:
        return int(beginning + element)
    else:
        return int(beginning + end + element)


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

# did a good job coding with intent followed the process! 10:36 mins