# Given the following data structure, return a new list identical in structure to the original but,
#  with each number incremented by 1. Do not modify the original data structure. Use a comprehension.

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

[{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]


def increment_value(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[key] = value + 1
    return new_dict

final_dict = [increment_value(dictionary) for dictionary in lst]


print(final_dict)
print(lst)

# print(new_dict)
# if we want to change somehting we must do it with a function argument 
# we cannot directly change it in a comprehension
