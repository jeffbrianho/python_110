# Write a function, persistence, that takes in a positive parameter
# `num` and returns its multiplicative persistence, which is the number
# of times you must multiply the digits in `num` until you reach a single digit.

"""
break into string to work with individual parts
determine the length and split into a list
multiply as an integer until you get a sum, 

while loop with counter 

repeat until len of sum == 1
helper function. string to integer list
product function

if len product == 1 end

"""
def create_num_list(num):
    str_num = str(num)
    str_num_list = list(str_num)
    int_num_list = [int(num) for num in str_num_list]

    return int_num_list

def product_of_list(num_list):
    index = 0
    product = 1

    while index < len(num_list):
        product *= num_list[index]
        index +=1 

    return product

def persistence(num):
    count = 0
    final_product = num
    while len(str(final_product)) != 1:
        final_product = product_of_list(create_num_list(final_product))
        count += 1

    return count


# Examples:

print(persistence(39)) # should return 3, because 3*9=27, 2*7=14, 1*4=4 and 4 has only one digit
print(persistence(999) == 4) # because 9*9*9=729, 7*2*9=126, 1*2*6=12, and finally 1*2=2
print(persistence(4) == 0) # because 4 is already a one-digit number
print(persistence(25) == 2) # because 2*5=10, and 1*0=0