# Given two lists of integers of the same length, return a new list where each element is 
# the product of the corresponding elements from the two lists.

"""
i: 2 list of same length ints
o: 1 list of products

idx range multiply 1 by other and return new list

"""

def multiply_items(list1, list2):
    return [list1[indx] * list2[indx] for indx in range(len(list1))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# 1:58 mins