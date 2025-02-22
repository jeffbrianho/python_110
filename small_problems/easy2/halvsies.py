# Write a function that takes a list as an argument and returns a list that contains 
# two elements, both of which are lists. Put the first half of the original list 
# elements in the first element of the return value and put the second half in the
#  second element. If the original list contains an odd number of elements, place the 
# middle element in the first half list.

"""
I list
O nested list
E return a list with two element lists: 1/2 in one 1/2 in other. if not even, put the extra in first list
I what is 1 element? 1 full other empty what if empty list? return 2 empty

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

D lists
A:
make place holder list
Take a list and determine its length
if even, use slicing to place half and half
if odd place larger half on one and other in rest
if 0, create two empty lists


"""

def halvsies(lst):
    split_list = []
    length = len(lst)
   
    if length % 2 == 0:
        split_list.append(lst[0:(length//2)])
        split_list.append(lst[(length//2):])
    else:
        split_list.append(lst[0:((length//2) + 1)])
        split_list.append(lst[((length//2) + 1):])
    
    return split_list




# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])


#Their answer

def halvsies(lst):
    half = (len(lst) + 1) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]