# Write a function that takes a list of numbers and returns the sum of the sums of 
# each leading subsequence in that list. Examine the examples to see what we mean. 
# You may assume that the list always contains at least one number.

"""
P
I list
O: int
E: list of number and returns sum of sums

E:

D:

A:

thing of sum of sublist - 0:1 0:2 0:3
sum[[list[:end] for end in range(1, len(list + 1))] 



"""

# def sum_of_sums(lst):
#     return sum([sum(lst[:end]) for end in range(1, len(lst) + 1)])

def sum_of_sums(lst):
    count = 0
    final_count = 0

    for num in lst:
        count += num
        final_count += count

    return final_count

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True