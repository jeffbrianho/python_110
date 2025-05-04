# Create a function that takes a single integer argument and returns 
# the sum of all the multiples of 7 or 11 that are less than the argument. 
# If a number is a multiple of both 7 and 11, count it just once.

# For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. 
# The sum of these multiples is 75.

# If the argument is negative, return 0.

"""
P:
I: integer
O: integer
E: multiples of 7 or 11 that are less than input (sum)
if negative return 0 
I

E
D
A
if num > 0 then continue
if num % 7 = 0 or num % 11 = 0 (and num < num can range up to number)
use a range
add to count until num

"""

def seven_eleven(arg):
    final_count = 0
    if arg > 0:
        for num in range(arg):
            if num % 7 == 0 or num % 11 == 0:
                final_count += num
        return final_count
    return 0

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)