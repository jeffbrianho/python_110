# Given the following data structure, return a new list with the same structure, 
# but with the values in each sublist ordered in ascending order as strings 
# (that is, the numbers should be treated as strings). Use a comprehension if you can.
#  (Try using a for loop first.)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

[['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

new_lst = []

for sublst in lst:
    new_lst.append(sorted(sublst, key=str))

print(new_lst == [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']])

new_lst = [sorted(sublst, key=str) for sublst in lst]
print(new_lst == [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']])