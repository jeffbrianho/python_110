# Write a function that combines two lists passed as arguments and returns a new list that contains 
# all elements from both list arguments, with each element taken in alternation.

# You may assume that both input lists are non-empty, and that they have the same number of elements.

def interleave(lst1, lst2):
    final_lst = []
    for indx in range(len(lst1)):
        final_lst.append(lst1[indx])
        final_lst.append(lst2[indx])

    return final_lst

def interleave(lst1, lst2):
   return ([ele for tup in zip(lst1, lst2)
           for ele in tup])



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

# 2 different ways 3:39 mins: append by length or use zip and unpack through nested for loop