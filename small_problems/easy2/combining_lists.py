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

