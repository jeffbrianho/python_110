# From two list arguments, determine the elements that are unique to the first list. 
# The return value should be a set.



# consider a difference

def unique_from_first(list1, list2):
    return set(list1) - set(list2)



list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

# second try 1 min 
def unique_from_first(list1, list2):
    return set(list1) - (set(list2))