# Create a function that takes a list of integers as an argument. 
# Determine and return the index N for which all numbers with an index 
# less than N sum to the same value as the numbers with an index greater than N. 
# If there is no index that would make this happen, return -1.

# If you are given a list with multiple answers, return the index with the smallest value.

# The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to
#  the right of the last element is 0.

"""
P
I: list
O: int
E
I

E
D
A
range through not including [0] 
first part and second part
if first part == second part return (indx)
else return -1 


"""

def equal_sum_index(lst):
    final = []
    for indx in range(len(lst)):
        first_portion = lst[:indx]
        second_portion = lst[indx + 1:]
        
        if sum(first_portion) == sum(second_portion):
            final.append(indx)
    if final:
        return final[0]
    else:
        return -1 

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3) 
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)