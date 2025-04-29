# Take the number 735291 and rotate it by one digit to the left, getting 352917.
#  Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. 
# Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits 
# fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and 
# rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the 
# original number.

# Write a function that takes an integer as an argument and returns the maximum rotation of that integer. 
# You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

"""
P
I: Integer
O: Integer
E: rotate each digit from left to right until maximum amount of rotations occur
I:

E
D strings
A:
convert digit to string:
have the function to rotate each by a count but use a range instead
for range(len(str)) iterate through each rotation
"""

def rotate_rightmost_digit(num, count):
    string_number = str(num)
    start_string = string_number[:count]
    end_string = string_number[count:]
    final_string = start_string + rotate_string(end_string)

    return (final_string)

def rotate_string(string):
    if len(string) > 0:
        return string[1:] + string[0]
    else:
        return '' 

def max_rotation(num):
    str_num = str(num)
    for count in range(len(str(num))):
        str_num = rotate_rightmost_digit(str_num, count)
    return int(str_num)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
print(max_rotation(105) == 15)               # True


# they did it without changing the original function. better to do this. !Use a reverse range

def max_rotation(number):
    number_digits = len(str(number))
    for count in range(number_digits, 1, -1):
        number = rotate_rightmost_digits(number, count)

    return number

# This will go through each char and swap to the end for each char until it hits every element. 