# Transform two lists into frozen sets and find their common elements.

"""
use frozenset conversion function
perform intersection to get common member

"""

def intersection(lst1, lst2):
    return frozenset(lst1) & frozenset(lst2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True