# Create a function that takes two integer arrays of equal length, 
# compares the value of each member in one array to the corresponding member in the other, 
# squares the absolute value difference between those two values, and 
# returns the average of those squared absolute value differences between each member pair.

# Examples
# [1, 2, 3], [4, 5, 6] --> 9 because (9 + 9 + 9) / 3
# [10, 20, 10, 2], [10, 25, 5, -2] --> 16.5 because (0 + 25 + 25 + 16) / 4
# [-1, 0], [0, -1] --> 1 because (1 + 1) / 2
"""
P
I: 2 integer arrays of equal length
O: returns the square of the absolute value difference between the two and returns the average div by the members
E: 
I
E
D: lists

A:
iterate through each list using enumerate and subtract/abs value into its own list?
div by the len of 1 list?
return the value



"""
def solution(lst1, lst2):
    difference_list = []
    
    for idx, element in enumerate(lst1):
        difference_list.append(abs(element - lst2[idx]))

    squared_lst = [num**2 for num in difference_list]

    summed_lst = sum(squared_lst)

    final_num = summed_lst/len(lst1)

    return final_num

print(solution([1, 2, 3], [4, 5, 6]) == 9)
print(solution([10, 20, 10, 2], [10, 25, 5, -2]) == 16.5)
print(solution([-1, 0], [0, -1]) == 1)