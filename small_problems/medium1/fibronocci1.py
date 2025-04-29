# The Fibonacci series is a sequence of numbers in which each number is the sum 
# of the previous two numbers. The first two Fibonacci numbers are 1 and 1. 
# The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, 
# the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

# F(1) = 1
# F(2) = 1
# F(n) = F(n - 1) + F(n - 2)    (where n > 2)

# Write a function called fibonacci that computes the nth Fibonacci number, 
# where nth is an argument passed to the function:

"""
P
I: Integer representing the location of the number
O: Integer representing The number at that location
E: only requires single integers as input
I

E print(fibonacci(3) == 2) the third number in this is 1, 1, 2 <


D: list to contain fibronocci numbers

A: create a list with all of the fibronocci numbers, use indexing to pull number:
num - 1 is the index we want: lst[num - 1]

create the fibronocci list?
    F1 = 1
    F2 = 2
    Fn = n - F1 + n - F2?

    1, 1, 2, 3, 5, 8, 13
    have a list with 1, 1
    take the list and append lst[-1] + lst[-2]
"""
fib_lst = [1, 1]

def fib_create(lst, num):
    for _ in range(num):
        lst.append(lst[-1] + lst[-2])
    return fib_lst

def fibonacci(num):
    return fib_create(fib_lst, num)[(num - 1)]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

# Their answer

def fibonacci(nth):
    if nth <= 2:
        return 1

    previous, current = 1, 1
    for _ in range(3, nth + 1):
        previous, current = current, previous + current

    return current