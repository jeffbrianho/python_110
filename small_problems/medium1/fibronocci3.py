# Memoization is an approach that involves saving a computed answer for future reuse, 
# instead of computing it from scratch every time it is needed. In the case of our recursive 
# fibonacci function, using memoization saves calls to fibonacci(nth - 2) because the necessary 
# values have already been computed by the recursive calls to fibonacci(nth - 1).

# For this exercise, your objective is to refactor the recursive fibonacci function to use memoization.

# Hint: One approach to memoization is to use a lookup table, such as an object, 
# for storing and accessing previously computed values.

def fibonacci(num): #3
    fib_dict = {}

    if num <= 2:
        return 1

    for key in range(num):
        fib_dict[key] = fibonacci(key)

    return fib_dict[num - 1] + fib_dict[num - 2]

"""
create a key value for each one

"""


print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True

# Their answer:

memo = {}
def fibonacci(nth):
    if nth <= 2:
        return 1
    elif nth in memo:
        return memo[nth]
    else:
        memo[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
        return memo[nth]