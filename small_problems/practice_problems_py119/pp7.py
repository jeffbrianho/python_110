

# Create a function that takes a list of integers as an argument and returns the number of 
# identical pairs of integers in that list. For instance, the number of identical pairs in 
# [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

# If the list is empty or contains exactly one value, return 0.

# If a certain number occurs more than twice, count each complete pair once. For instance, 
# for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. The first list contains
#  two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

"""
P
I: list of integers
O: number of identical pairs  int
E: return 0 for empty or 1 value
I: must complete the pair

E
D: dic count and floor divide by 2
A

can create a num/count dict and if value is >=2 floor divide and add to count

"""

def pairs(lst):
    num_count_dict = {num: lst.count(num) for num in lst}
    
    count = 0

    for _, value in num_count_dict.items():
        if value >= 2:
            count += value // 2
    
    return count

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)


# finished in 4:24 mins