# Write a function that takes one argument, a positive integer, and returns the sum of its digits.

"""
return sum(int(str(num))
"""

def sum_digits(num):
    return sum([int(num) for num in str(num)])

print(sum_digits(23))# == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

# 1:30 mins