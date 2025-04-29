import sys

sys.set_int_max_str_digits(50_000)

"""
I: integer representing digit length
O: integer representing the index with the first starting at 1

e: 2 digit number starts at index "7" 6 for a list
    3 starts at "12" 11 etc

    
d list? for indexing capabilities
strings to use len function
find lenof num enumerated? for indexd numbers
return index of

"""

def fibonacci(nth):
    if nth <= 2:
        return 1

    previous, current = 1, 1
    for _ in range(3, nth + 1):
        previous, current = current, previous + current

    return current

def find_fibonacci_index_by_length(num):
    count = 1
    while len(str(fibonacci(count))) < num:
        count += 1
    
    
    return count
    

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# # Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)


# Their answer
import sys

def find_fibonacci_index_by_length(length):
    sys.set_int_max_str_digits(50_000)
    first = 1
    second = 1
    count = 2

    while len(str(second)) < length:
        first, second = second, first + second
        count += 1

    return count

# Discussion

# The function starts by initializing the first two numbers in the Fibonacci sequence, both of which, by definition, are 1. We use the count variable to keep track of where we are in the sequence -- the value of second is the second Fibonacci number, so our count is initially 2.

# The solution then uses a while loop to calculate the value of each subsequent Fibonacci number while the length of the number is less than the value of the length argument. At every iteration, the solution does the following:

# The values of first and second are updated by using Python's tuple unpacking feature: first, second = second, first + second. This line simultaneously updates first to the value of second and second to the sum of first and second.
# We increment count by 1.
# Once a Fibonacci number with the desired number of digits is found, the loop stops and the function returns the count.