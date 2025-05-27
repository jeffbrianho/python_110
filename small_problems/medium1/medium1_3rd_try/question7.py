# The Fibonacci series is a sequence of numbers in which each number is the sum 
# of the previous two numbers. The first two Fibonacci numbers are 1 and 1. 
# The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, 
# the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

def fibonacci(num):

    current_num = 1
    prev_num = 0

    if num < 2:
        return 1
    
    for _ in range(num - 1 ):
        current_num, prev_num = prev_num + current_num, current_num 
    
    return current_num

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

# 7 mins