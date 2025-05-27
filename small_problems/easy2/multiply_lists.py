# Write a function that takes two list arguments, each containing a list of numbers, 
# and returns a new list that contains the product of each pair of numbers from the 
# arguments that have the same index. You may assume that the arguments contain the same number of elements.

"""
p
I 2 lists of numbers
O new list with returns product of numbers from same index
E same elements
I

e
d
a:
go through each and append to a new list the product of each list at index access
return list


"""

def multiply_list(lst1, lst2):
    new_lst = []

    index = 0

    for num in lst1:
        new_lst.append(num * lst2[index])
        index += 1

    return new_lst

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

#zip
def multiply_list(numbers1, numbers2):
    return [a * b for a, b in zip(numbers1, numbers2)]

# second answer

def multiply_list(lst1, lst2):
    return [lst1[indx] * lst2[indx] for indx in range(len(lst1))]