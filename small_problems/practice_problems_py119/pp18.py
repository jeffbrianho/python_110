# Create a function that takes a list of integers as an argument. 
# Determine and return the index N for which all numbers with an index less than N sum to the 
# same value as the numbers with an index greater than N. If there is no index that would make 
# this happen, return -1.

# If you are given a list with multiple answers, return the index with the smallest value.

# The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to 
# the right of the last element is 0.


"""
P
I: LIST of int
O: INT 
E: N SUM TO THE SAME VALUE index less vs sum indx greater than N not including N when this is the case  they are equal
I

E:  left must equal right side 
D: list with sums 

A:
iterate through the indices and create a list that compares
2 lists index[0:indx(0)] number is non-inclusive , (indx+1 : )
    - for lst[:indx] range(len(lst))
        if indx = 0 and lst[indx + 1:] == 0
            return index
        if indx == len(lst) and lst[len(lst):] == 0
            return index
        if lst[:indx] == lst[indx+1:]
            return indx
        else:
            return -1

return the index when list1 == list 2 and the smallest:


when indx = 0 list 1 == 0 or when  indx = len(lst) -1 list 2 == 0


"""

def equal_sum_index(lst):
    for indx in range(len(lst)):
        if indx == 0 and sum(lst[indx + 1:]) == 0:
            return indx
        if indx == len(lst) and sum(lst[len(lst):]) == 0:
            return indx
        if sum(lst[:indx]) == sum(lst[indx + 1:]):
            return indx
   
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

# 17 mins didnt check throughout should do that coded before tested
