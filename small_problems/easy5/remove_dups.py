# Given a sequence of integers, filter out instances where the same value occurs successively,
#  retaining only the initial occurrence. Return the refined sequence.


"""
P:
    I: List of int
    O: filter out repeats if consecutive numbers
    E
    I

E:

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

D:

A:
final_lst
iterate through list and append to final list
if final list is empty or [-1] != append

"""


def unique_sequence(lst):
    final_lst = []
    for num in lst:
        if not final_lst or final_lst[-1] != num:
            final_lst.append(num)

    return final_lst


#Their answer
def unique_sequence(numbers):
    if not numbers:
        return []

    unique = [numbers[0]]
    for value in numbers[1:]:
        if value != unique[-1]:
            unique.append(value)

    return unique

def unique_sequence(numbers):
    return [value
            for idx, value in enumerate(numbers)
            if idx == 0 or value != numbers[idx-1]] # use the last index to compare as iterating through idx

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original))# == expected)      # True