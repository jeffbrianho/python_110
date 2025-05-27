# Write a function that takes a list as an argument and reverses its elements, in place. 
# That is, mutate the list passed into the function. The returned object should be the same 
# object used as the argument.

# You may not use the list.reverse method nor may you use a slice ([::-1]).

"""
I list
O list
E: reversed elements in place : mutates
cannot use reverse or slice ::-1
reverse the list not the elements
empty list is empty


d list with index counter
reassignment 0 - end 1 to end - 1

iterate through the index 1/2 length of list
if 5 // 2 == 2 
reassign index 0 to index 4 and 1 to index 3
if even same thing

return same list:


"""

def reverse_list(lst):
    half_length = len(lst) // 2

    for index in range(half_length):
        lst[index], lst[len(lst) -1 - index] = lst[len(lst) -1 - index], lst[index]

    return lst 

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

# took time to write it out. 8:40 seconds