# Create a function that takes a single integer argument and returns the sum of all 
# the multiples of 7 or 11 that are less than the argument. If a number is a multiple 
# of both 7 and 11, count it just once.

# For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. 
# The sum of these multiples is 75.

# If the argument is negative, return 0.

"""
P
I: int
O: int
E: sum of all the multiples of 7 or 11 that are less than argument
negatives return 0 
I

E: 10 7
12 - 7, 11 = 18
D: ranges to get all the numbers 7 / 11 up to number
list to hold all numbers
A:
if num < 0 return 0  
make a range to the number given with selection criteria of
num % 7 or num % 11
return sum of list

"""

def seven_eleven(num):
    if num < 0:
        return 0 

    return sum([dig for dig in range(num)
            if dig % 7 == 0 or dig % 11 == 0])




print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

# 4:30 mins