# Your goal is to write the group_and_count method, which should receive an array
# as a unique parameter and return a hash. Empty or nil input must return nil
# instead of a hash. This hash returned must contain as keys the unique values
# of the array, and as values the counting of each value.

"""
P
I: array
O: hash
E: empty or nil return nil instead of has
I


E: looks like return a dictionary with the unique nums as keys and count as values
D: dict
A
too easy to do..
"""

def group_and_count(lst):
    if lst:
        return {num: lst.count(num) for num in set(lst)}

print(group_and_count([1,1,2,2,2,3]) == {1: 2, 2: 3, 3: 1})
print(group_and_count([]) == None)
print(group_and_count(None) == None)
print(group_and_count([1, 7, 5, -1]) == {1: 1, 7: 1, 5: 1, -1: 1})

# Time to complete: 3:56 mins
# Theme - create a dictionary comprehension
# same as theme