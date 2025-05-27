# Given a sequence of integers, filter out instances where the same value occurs successively, 
# retaining only the initial occurrence. Return the refined sequence.

"""
add to save list if save list[-1] == to num continue, 

"""

def unique_sequence(lst):
    saved_list = []
    for num in lst:
        if saved_list:
            if num == saved_list[-1]:
                continue
            else:
                saved_list.append(num)
        else:
            saved_list.append(num) # gets first number

    return saved_list

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True