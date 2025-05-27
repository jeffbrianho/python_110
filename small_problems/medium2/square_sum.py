# Write a function that computes the difference between the 
# square of the sum of the first count positive integers and the sum of 
# the squares of the first count positive integers.

"""
P
I: an integer
O: an integer that is the differnce between the sum factorial and the square sum factorial.
E: only whole numbers and positive numbers
I

E
D ints
A:

get the first factorial; use import math factorial or
range from num - 0 -1 add to count
list range num - 0 -1 sum(square) comprehension
num2 - num 1 return 


"""
def sum_square_difference(num):
    unsquared_sum = sum(list(range(num, 0, -1)))
    squared_sum = sum([value**2 for value in range(num, 0, -1)])
    return ((unsquared_sum**2) - squared_sum)



print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

# Their answer

def sum_square_difference(count):
    sum_ = sum(range(1, count + 1))

    sum_of_squares = 0
    for i in range(1, count + 1):
        sum_of_squares += i**2

    return sum_**2 - sum_of_squares

# my second answer 6:25 mins

def sum_square_difference(num):
    sum_squared = sum([dig for dig in range(1, num + 1)])**2
    squared_sum = sum([dig**2 for dig in range(1, num + 1)])

    return sum_squared - squared_sum
