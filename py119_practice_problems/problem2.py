# Create a function that takes a list of integers as an argument. 
# The function should return the minimum sum of 5 consecutive numbers in the list. 
# If the list contains fewer than 5 elements, the function should return None.


"""
i:list 
o:int or None
e: min sum of numbers consecutive 5. if less than 5 return none
i

E
D: list of 5 consecutive elements: 

A: check if list is 5 or greater return
iterate through each one and get each sub 5 num elements and provide sum, return the smallest

first create the condition for none
then:
start with 0:5 then 1-6 etc to get all possible lists of 5 

"""

def minimum_sum(lst):
    if len(lst) >=5:
        consecutive_num_lst = [lst[idx:idx + 5] for idx in range(len(lst))
                                if len(lst[idx:idx + 5]) == 5]
        return min([sum(lst) for lst in consecutive_num_lst])

    else:
        return None

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)