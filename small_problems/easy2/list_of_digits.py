# Write a function that takes one argument, a positive integer, and 
# returns a list of the digits in the number.

"""
I: int
O: list of digits in num

A: change to str to iterate
sep by list constructor
pot int chain?


"""

def digit_list(num):
    s = str(num)
    lst = list(s)

    final_lst = []

    for ele in lst:
        final_lst.append(int(ele))

    return final_lst

#their answer

def digit_list(number):
    return [int(digit) for digit in str(number)]


print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

def digit_list(num):
    str_num = str(num)
    list_str = list(str_num)

    return [int(num) for num in list_str]