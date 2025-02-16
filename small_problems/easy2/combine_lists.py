# Write a function that combines two lists passed as arguments and returns a new list that
#  contains all elements from both list arguments, with each element taken in alternation.

# You may assume that both input lists are non-empty, and that they have the same number of elements.

"""


"""

def interleave(lst1, lst2):
    tup_list = list(zip(lst1, lst2))
    final_lst = []

    for el1, el2 in tup_list:
        final_lst.append(el1)
        final_lst.append(el2)
  
    return final_lst


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

# Their answer

def interleave(list1, list2):
    new_list = []
    for idx in range(len(list1)):
        new_list.extend([list1[idx], list2[idx]])

    return new_list