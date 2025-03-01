# You want to multiply all elements of a list by 2.
#  However, the function is not returning the expected result.
#  Explain the bug, and provide a solution.


# def multiply_list(lst):
#     for item in lst:
#         item *= 2

#     return lst

# print(multiply_list([1, 2, 3]) == [2, 4, 6])

# we are not capturing or mutating the list we need to do something with the item in the 
# list perhaps with with list reassignment

# def multiply_list(lst):
#     for indx in range(len(lst)):
#         lst[indx] *= 2

#     return lst

# print(multiply_list([1, 2, 3]) == [2, 4, 6])

# or we can capture to a new list if we do not want to mutate

def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])