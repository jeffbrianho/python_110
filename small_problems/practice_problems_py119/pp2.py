# Create a function that takes a list of integers as an argument. 
# The function should return the minimum sum of 5 consecutive numbers in the list.
#  If the list contains fewer than 5 elements, the function should return None.


"""
p
I: list of ints
O: int min sum of 5 consecutive numbers in list
E: if lst less than 5 return None
I

e: consecutive means in the list so 0:5 1:6 etc
d: lists containing 5 elements in list

a:
create a list of sublists that contain all consecutive 5 elements
sum each one and return the min amount

iterate for start to end for length of list + 4 and save list that are a length of 5
range(len(lst)) if len is > 5

sum for each list, return min


"""

def minimum_sum(lst):
    if len(lst) < 5:
        return None

    sub_lsts = min([sum(lst[indx:indx + 5]) for indx in range(len(lst))
                if len(lst[indx:indx + 5]) == 5])
    return sub_lsts

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

## 11:35 mins iterating through range