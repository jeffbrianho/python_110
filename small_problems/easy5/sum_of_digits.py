# Write a function that takes one argument, a positive integer, and returns the sum of its digits.


"""
P
I integer positive
O sum of its digits
E
I

E
print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

D Strings and counter

A:
count = 0
convert num to string to be able to iterate
convert each char to num and have a counter +=
return counter

"""

def sum_digits(num):
    # sum_total = 0
    # for char in str(num):
    #     sum_total += int(char)
    # return sum_total 

#can we do this as a comprehension?
# maybe a list

    return sum([int(char) for char in str(num)])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True