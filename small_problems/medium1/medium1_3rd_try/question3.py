# Take the number 735291 and rotate it by one digit to the left, getting 352917. 
# Next, keep the first digit fixed in place and rotate the remaining digits to get 329175.
#  Keep the first two digits fixed in place and rotate again to get 321759. 
# Keep the first three digits fixed in place and rotate again to get 321597. 
# Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. 
# The resulting number is called the maximum rotation of the original number.

# Write a function that takes an integer as an argument and returns the maximum rotation of that integer. 
# You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

"""
P
I: integer
O: integer
E: perform consecutive rotations: rotating the length of the digit times

I

E: if 0 at end when int should solve
D: range for the consecutive rotations
A: 
find length of digit by turning into string
    -len(Str(num))
use range for loop of length
    (_ range of negative number ::-1)
change the first digit for a (+) place and reassign 
    call rotate rightmost digit
    reassignment? 
    
continue until end of digit string
return the final string as integer

C
"""
def max_rotation(num):
    length = len(str(num))
    str_num = str(num)
    for indx in range(length, 1, -1):
        str_num = rotate_rightmost_digits(str_num, indx)

    return int(str_num)

def rotate_rightmost_digits(number, place):
    str_num = number

    element = str_num[-place]
    beginning = str_num[:-place]
    end = str_num[-place + 1:]

    if place == 1:
        return (beginning + element)
    else:
        return (beginning + end + element)
    


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

# 20:33 mins needed to change all to a string. may have been faster if I started from scratch but had to manipulate
# the other functino to ensure it stayed a string. 