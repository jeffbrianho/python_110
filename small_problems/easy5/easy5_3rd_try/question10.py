# Given a sequence of integers, filter out instances where the same value occurs successively,
#  retaining only the initial occurrence. Return the refined sequence.

"""

use save value
append number to empty list
if next number is == [-1 ] from saved list
continue
else append
return list
"""

def unique_sequence(lst):
    final_lst = []
    for num in lst:
        if not final_lst:
            final_lst.append(num)
        elif num != final_lst[-1]:
            final_lst.append(num)

    return final_lst
    

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True