# Given the following data structure return a new list identical in structure to the original,
#  but containing only the numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

[[], [3, 12], [9], [15, 18]]


# new_list = []

# for sublist in lst:
#     new_sublist = []

#     for number in sublist:
#         if number % 3 == 0:
#             new_sublist.append(number)

#     new_list.append(new_sublist)

# print(new_list)

# def is_multiple_3(sublist):
#     new_sublist = []
#     for number in sublist:
#         if number % 3 == 0:
#             new_sublist.append(number)
#     return new_sublist

# new_list =[is_multiple_3(sublist) for sublist in lst]

# print(new_list)

#their answers

# def divisible_by_3(sublist):
#     return [num for num in sublist if num % 3 == 0]

# new_list = [divisible_by_3(sublist) for sublist in lst]
# print(new_list)

# new_list = []

# for sublist in lst:
#     new_sublist = [num for num in sublist if num % 3 == 0]
#     new_list.append(new_sublist)

# print(new_list)

new_list = [[num for num in sublist if num % 3 == 0] for sublist in lst]

print(new_list)

#can create a nested list

# 2 MAJOR TACTICS: Using functions to modify an output or using a nested list

