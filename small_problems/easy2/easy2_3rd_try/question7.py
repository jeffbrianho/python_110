# Write a function that takes two list arguments, each containing a list of numbers, 
# and returns a new list that contains the product of each pair of numbers from the arguments 
# that have the same index. You may assume that the arguments contain the same number of elements.

def multiply_list(lst1, lst2):
    final = []

    for indx in range(len(lst1)):
        final.append((lst1[indx] * lst2[indx]))

    return final

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# 2:07 mins straight forward