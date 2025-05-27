# Write a function that rotates a list by moving the first element to the end of the list. 
# Do not modify the original list; return a new list instead.

# If the input is an empty list, return an empty list.
# If the input is not a list, return None.
# Review the test cases below, then implement the solution accordingly.


"""
P
I: list
O: list new
E: new list with first element moved to end of list copy
if empty - return empty
if not a list return None
I

E

D:lists

A:
Determine if object is list - return None if not
Determine if the list is empty - return copied empty list?
Use pop method of index 0 and addend from a copy of the list? or use slicing?
return copied list

"""

def rotate_list(lst):
    new_lst = []
    if type(lst) == list:
        if lst:
            new_lst = lst[1:]
            new_lst.append(lst[0]) # can do lst[1:] + [lst[0]]!
            return new_lst
        else:
            return new_lst

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

#This will replace the first element in the list to the last without mutating the original. 

# Their answer
def rotate_list(lst):
    if not isinstance(lst, list):
        return None

    if len(lst) == 0:
        return []

    return lst[1:] + [lst[0]]

# my second answer 5:49 mins
def rotate_list(lst):
    final_list = []

    if type(lst) != list:
        return None
    
    if lst:
        final_list.extend(lst[1:])
        final_list.append(lst[0])
    
    return final_list