# Given two lists, convert them to sets and return a new set which is the union of both sets.


"""
I two lists
O a merged set unionized


can use a set coersion then merge

"""

def merge_sets(lst1, lst2):
    
    merged_set = set(lst1) | set(lst2)

    return(merged_set)

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

# attempt 2
def merge_sets(lst1, lst2):
    return set(lst1) | set(lst2)
# time 1 min