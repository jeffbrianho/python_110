# Write a function that takes a list as an argument and reverses its elements,
#  in place. That is, mutate the list passed into the function. 
# The returned object should be the same object used as the argument.

# You may not use the list.reverse method nor may you use a slice ([::-1]).

"""
p
I list
O same list reversed
E
I
e
d dictionary to hold index and element enumerate?
index reassignment?

a
list a b c

dict 0 a 1 b 2 c
inverse count = lenlist
count = 0
list[inverse count 2] = value[count 0]
1 1 
0  2


"""

def reverse_list(lst):
    storage_dict = {}

    count = 0
    inverse_count = len(lst) - 1

    for idx, num in enumerate(lst):
        storage_dict[idx] = num

    while inverse_count >= 0:
        lst[inverse_count] = storage_dict[count]
        inverse_count -= 1
        count += 1

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

# my answer
def reverse_list(lst):
    copy_lst = lst[:]
    lst.clear()
    for indx in range(len(copy_lst) - 1, -1, -1):
        lst.append(copy_lst[indx])  
    return lst
