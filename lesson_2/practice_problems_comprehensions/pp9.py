# Given the following data structure, write some code to return a list that 
# contains only the dictionaries where all the numbers are even.

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# [{e: [8], f: [6, 10]}]

"""
O: list of dictionaries if nums are even
[{}]

a: will need to use the all([num % 2 == 0]) list comprehension
start with creating a list with dictionaries
get to the value of nested dictionary
go through each element with the list comprehension above and only append if meets criteria
"""

final_list = []
for dictionary in lst:
    values_list = []
    for value in dictionary.values():
        values_list.append(all([num % 2 == 0 for num in value]))
    if all(values_list):
        final_list.append(dictionary)

print(final_list == [{'e': [8], 'f': [6, 10]}]
)

