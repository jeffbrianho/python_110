# Write a method that takes an array of consecutive (increasing) letters as input
# and that returns the missing letter in the array.
# You will always get an valid array. And it will be always exactly one letter be missing.
# The length of the array will always be at least 2.
# The array will always contain letters in only one case.
# Example:
# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'
"""
P
I: array of consecutive letters
O: returns missing letter
E: will always be a valid array and missing only 1 letter, len at least 2 and in 1 case
I

E
D:list of reference? caps and non caps?
A:
iterate through list and return when it does not match alphabet

create a reference list of non_caps and caps: X
determine starting point if caps or non caps on given list
find matching letter for starting point on reference. ex find reference.find(lst[0])
use that index as starting point and follow by index until index of the reference does not match the lst
return that letter from reference


"""
def find_missing_letter(array):
    NON_CAP_REFERENCE_LIST = list('abcdefghijklmnopqrstuvwxyz')
    CAP_REFERENCE_LIST = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if array[0].isupper():
        reference_index = CAP_REFERENCE_LIST.index(array[0])
        for char in array:
            if char == CAP_REFERENCE_LIST[reference_index]:
                reference_index += 1
                continue
            else:
                return CAP_REFERENCE_LIST[reference_index]
    else:
        reference_index = NON_CAP_REFERENCE_LIST.index(array[0])
        for char in array:
            if char == NON_CAP_REFERENCE_LIST[reference_index]:
                reference_index += 1
                continue
            else:
                return NON_CAP_REFERENCE_LIST[reference_index]
    
print(find_missing_letter(['a','b','c','d','f']) == 'e')
print(find_missing_letter(['O','Q','R','S']) == 'P')

# Time to complete: 11:55 mins
# Theme: iterating through conditions for consecutive alphabet
# Approach: use a reference list, simultaneous iteration using continue and "break" statements (return used
# for break statement)