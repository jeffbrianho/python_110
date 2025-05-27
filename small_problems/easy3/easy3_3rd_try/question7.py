# Write a function that takes a string argument consisting of a first name, a space, and a last name.
#  The function should return a new string consisting of the last name, a comma, a space, and the first name.

def swap_name(names):
    list_name = names.split()
    return f'{list_name[1]}, {list_name[0]}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# less than a min
