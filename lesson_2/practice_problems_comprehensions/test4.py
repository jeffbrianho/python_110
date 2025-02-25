# Use a nested dictionary comprehension to create a new dictionary that contains only the 
# subjects where each student scored above 85.

grades = {
    'Alice': {'Math': 85, 'Science': 90, 'English': 92},
    'Bob': {'Math': 78, 'Science': 85, 'English': 80},
    'Charlie': {'Math': 92, 'Science': 88, 'English': 95}
}

#return 'Charlie': {'Math': 92, 'Science': 88, 'English': 95}

# for name, subdict in grades.items():
#     grade_list = [grade for grade in subdict.values()]

#     if all([(num > 85)for num in grade_list]):
#         new_dict = {name: subdict}
#         print(new_dict)

# def make_list(nums):
#     return [num for num in nums]

# new_dict = {name:subdict for name, subdict in grades.items()
#             if all([(num > 85)for num in make_list(subdict.values())])}

# print(new_dict)

new_dict = {name: subdict for name, subdict in grades.items()
            if all(grade > 85 for grade in subdict.values())}