# Given the following data structure, return a new list with the same structure, 
# but with the values in each sublist ordered in ascending order. Use a comprehension 
# if you can. (Try using a for loop first.)


lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]



[['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]


# new_lst = []
# for sublst in lst:
#     new_lst.append(sorted(sublst))

# print(new_lst)

new_lst = [sorted(sublst) for sublst in lst]

print(new_lst)

# The string values should be sorted as strings, while the numeric values should be sorted as numbers.