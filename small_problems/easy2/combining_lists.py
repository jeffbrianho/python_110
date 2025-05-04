# Write a function that takes two lists as arguments and returns a set that contains the union
#  of the values from the two lists. You may assume that both arguments will always be lists.


"""
2 lists
set 
union of two lists
E:
D: lists and sets
a: extend the list?
convert to set?


"""
def union(lst1, lst2):
    lst1.extend(lst2)
    return set(lst1)


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

#Their ansewr
def copy_non_dups_to(result_set, lst):
    for value in lst:
        result_set.add(value)

def union(list1, list2):
    result_set = set()
    copy_non_dups_to(result_set, list1)
    copy_non_dups_to(result_set, list2)
    return result_set

def union(list1, list2):
    return set(list1).union(set(list2))

# my second answer

def union(lst1, lst2):
    return (set(lst1) | set(lst2))