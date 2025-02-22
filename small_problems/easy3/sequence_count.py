# Create a function that takes two integers as arguments. The first argument is a count, 
# and the second is the starting number of a sequence that your function will create. 
# The function should return a list containing the same number of elements as the count argument.
#  The value of each element should be a multiple of the starting number.

# You may assume that count will always be an integer greater than or equal to 0.
# The starting number can be any integer. If the count is 0, the function should return an empty list.


"""
P
I 2 int, 1 count, 2 starting numb
O list same elements as count ascending multiples of starting number
E count >= 0; 0 is an empty list
I

E
D
A

take starting number
use range of count to perform append each time
add the += of itself



"""

def sequence(count, num):
    lst = []
    new_num = 0
    for _ in range(count):
        new_num += num
        lst.append(new_num)
    return lst

#Their answer

def sequence(count, start_num):
    return [start_num * num for num in range(1, count + 1)]


print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True