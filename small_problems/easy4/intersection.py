# Transform two lists into frozen sets and find their common elements.


def intersection(lst1, lst2):
    return frozenset(lst1).intersection(frozenset(lst2))
# can also use &

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

# second attempt 1 min
def intersection(list1, list2):
    return frozenset(list1) & frozenset(list2)