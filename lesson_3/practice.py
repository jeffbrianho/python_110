# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the 
# "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). 
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121,
#  20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. 
# It gets obvious if we write b's elements in terms of squares:


"""

I: 2 lsts of integers
O: boolean

E
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

iterate through each number in array1 and determine create new list of squares
if new list is in list 2 return TRUE
False otherwise


"""
import math

def comp(array1, array2):

    sq_lst = [num**2 for num in array1]
    desq_lst = [math.sqrt(num) for num in array2]

    valid_lst = [sq_num in array2 for sq_num in sq_lst]
    valid_lst2 = [desq_num in array1 for desq_num in desq_lst]

    if len(array1) == len(array2):
        return all(valid_lst + valid_lst2)
    else:
        return False

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

print(comp(a, b))