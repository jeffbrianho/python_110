# Write a function that takes a list as an argument and returns a list that contains two elements, 
# both of which are lists. Put the first half of the original list elements in the first element of t
# he return value and put the second half in the second element. If the original list contains an 
# odd number of elements, place the middle element in the first half list.

"""
find the length of the list
make it the half number
if even return :half half:
return twos lists with slicing [: half+1] [half + 1 ] if uneven
"""

def halvsies(lst):
    half_length = len(lst) // 2
    
    if len(lst) % 2 == 0:
        return [lst[:half_length],lst[half_length:]]
    else:
        return [lst[:half_length + 1], lst[half_length + 1:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

# 4:50 seconds, took time to figure out that the lst slice returns a list again and not the elements by itself
