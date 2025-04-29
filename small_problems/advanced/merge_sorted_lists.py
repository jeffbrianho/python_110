# Write a function that takes two sorted lists as arguments and returns a new list 
# that contains all the elements from both input lists in ascending sorted order. 
# You may assume that the lists contain either all integer values or all string values.

# You may not provide any solution that requires you to sort the result list. 
# You must build the result list one element at a time in the proper order.

# Your solution should not mutate the input lists.


"""
P
I: 2 sorted lists
O: 1 new list sorted ascending order; ints or all str
E: no sort method 1 element at a time, do not mutate
I

E: takes 2 lists and sorts in ascending order without sort method
D: list structures comparison operators
A:
combine into 1 list first?
iterate through a while loop
if element 1 is more than previous replace? 
use a on off switch and a while true loop

PSEUDO:
for element in lst 1 addend
for element in lst 2 addend
for element in new_lst if element more than next replace indexes, toggle switch to (or keep true)
if no replacements toggle switch to false or break
return newlist

C


"""

def merge(lst1, lst2):
    mod_lst = []
    for ele in lst1:
        mod_lst.append(ele)
    for ele in lst2:
        mod_lst.append(ele)

    toggle = True
    while toggle:
        toggle = False
        for indx, element in enumerate(mod_lst):
            if indx + 1 < len(mod_lst) and element > mod_lst[indx + 1]:
                mod_lst[indx], mod_lst[indx + 1] = mod_lst[indx + 1], element
                toggle = True

    return(mod_lst) # [1, 5, 9, 2, 6, 8] >> [1, 5, 2, 6, 8, 9]

# # All of these examples should print True
# print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
# print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
# print(merge([], [1, 4, 5]) == [1, 4, 5])
# print(merge([1, 4, 5], []) == [1, 4, 5])

# names1 = ['Alice', 'Kim', 'Pete', 'Sue']
# names2 = ['Bonnie', 'Rachel', 'Tyler']
# names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
#                   'Rachel', 'Sue', 'Tyler']
# print(merge(names1, names2) == names_expected)

# # Their answers
# def merge(list1, list2):
#     copy1 = list1[:]
#     copy2 = list2[:]
#     result = []

#     while copy1 and copy2:
#         if copy1[0] <= copy2[0]:
#             result.append(copy1.pop(0))
#         else:
#             result.append(copy2.pop(0))

#     return result + copy1 + copy2