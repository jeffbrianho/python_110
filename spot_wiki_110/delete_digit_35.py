# Given an integer n, find the maximal number you can obtain by deleting
# exactly one digit of the given number.

"""
make a string
get all possible substrings and convert to num
use max
"""

def delete_digit(num):
    string_num = list(str(num))
    num_list = []

    for indx in range(len(string_num)):
        missing_num_list = string_num[:indx] + string_num[indx + 1:]
        num_list.append(int(''.join(missing_num_list)))

    return max(num_list)

 

print(delete_digit(152) == 52)
print(delete_digit(1001) == 101)
print(delete_digit(10) == 1)