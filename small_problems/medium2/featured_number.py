# A featured number (something unique to this exercise) is an odd 
# number that is a multiple of 7, with all of its digits occurring 
# exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 
# 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

# Write a function that takes an integer as an argument and returns the next 
# featured number greater than the integer. Issue an error message if there is no next featured number.

# NOTE: The largest possible featured number is 9876543201.


"""
P
I: integer
O: next featured number or error if none
E: odd number that is a multiple of 7 with no reoccuring digits
I: return either a digit or a string

E
D: ranges; ints strings

A:
take the number: find the closest number that is a multiple of 7 
check if that number is odd, and break into a string to assess repeating numbers. functions is odd, is not repeating
if false add 7 and check again loop until True. if not true provide error





"""
def is_odd(num):
    if num % 2 != 0:
        return True
    return False

def no_repeating_digits(num):
    string_num = str(num)
    repeat_list = []
    for indx in range(len(string_num)): 
        if len(string_num) != 1:
            repeat_list.append(string_num[indx] in string_num[indx + 1:])
        
    if any(repeat_list):
        return False
    return True

def nearest_multiple_of_7(num):
    for additional in range(1,8):
        if (num + additional) % 7 == 0:
            return num + additional  
        

def next_featured(num):
    finish = True
    while finish:
        next_num = nearest_multiple_of_7(num)
        if no_repeating_digits(next_num) and is_odd(next_num):
            return next_num 
        elif next_num == 9876543201 or num == 9876543201:
            return "There is no possible number that fulfills those requirements."
        else:
            num = next_num



print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

# Their answer
def to_odd_multiple_of_7(number):
    number += 1
    while number % 2 == 0 or number % 7 != 0:
        number += 1

    return number

def all_unique(number):
    digits = list(str(number))
    return len(digits) == len(set(digits))

def next_featured(number):
    MAX_FEATURED = 9876543201
    featured_num = to_odd_multiple_of_7(number)

    while featured_num <= MAX_FEATURED:
        if all_unique(featured_num):
            return featured_num

        featured_num += 14

    return "There is no possible number that fulfills those requirements."

# use a set to elimiate all numbers and if the lengths are the same. there are no repeat digits.
