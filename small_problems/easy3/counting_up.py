# Write a function that takes an integer argument and returns a list containing 
# all integers between 1 and the argument (inclusive), in ascending order.

# You may assume that the argument will always be a positive integer.


"""

p
i int
o list
e int between 1 and argument inclusive in ascending order
i all positive

e
d int lit
range

a
create a range to +1 argument
turn into list?

"""

def sequence(num):
    return list(range(1,num+1))
# myanswer
def sequence(num):
    return [num for num in range(1, num + 1)]


print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True