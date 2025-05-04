# Create a function that takes a list of integers as an argument and returns the number of
#  identical pairs of integers in that list. For instance, the number of identical pairs in 
# [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

# If the list is empty or contains exactly one value, return 0.

# If a certain number occurs more than twice, count each complete pair once.
#  For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. 
# The first list contains two complete pairs while the second has an extra 2 that 
# isn't part of the other two pairs.


"""
P
I: list
O: int
E
I

E
D dictioanry count. divide the count /2 and add to final count
A:
create a dictionary of num:count 
if count is > 1, // 2 and add the num to count
return count

"""

def pairs(lst):
    dict_of_nums = {num: lst.count(num) for num in lst}
    
    num_of_pairs = 0

    for num, count in dict_of_nums.items():
        if count > 1:
            num_of_pairs += count // 2
    
    return num_of_pairs

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

# 5 mins