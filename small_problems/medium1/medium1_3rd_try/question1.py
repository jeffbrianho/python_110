# Write a function that rotates a list by moving the first element to the end of the list. 
# Do not modify the original list; return a new list instead.

# If the input is an empty list, return an empty list.
# If the input is not a list, return None.
# Review the test cases below, then implement the solution accordingly.

"""
P
I: list
O: list

E: return the list with the first element at the end
if empty list return empty list
if no list return None
must mutate the list
I

E: 

D: lists mutations, 

A:
check to see if isinstance is list:
return None if not. 

    if empty list
    return empty list 

    if list is not empty

    new_list = lst[1:] + [lst[0]] makes copies
          
    return list

"""

def rotate_list(lst):
    if isinstance(lst, list):
        
        if lst:
            new_lst = lst[1:] + [lst[0]]

            return new_lst
        else:
            return []
        
    else:
        return None

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

# misread the question and mutated the list with a pop and append method. 13:02 mins
# had trouble with isinstance function never used. 