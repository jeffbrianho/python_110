# Write a function that takes a list of positive integers as input, 
# multiplies all of the integers together, divides the result by the number of 
# entries in the list, and returns the result as a string with the value rounded 
# to three decimal places.
"""  
P
I list of positive integers
O string of average 
E rounded to 3 decimals formatted_num = f"{num:.3f}"
I
Q

E
D
A
use average function?
return number with f mod?



"""


def multiplicative_average(lst):
    multiplied_lst = [1]
    for num in lst:
        multiplied_lst.append(num * multiplied_lst[-1])
   
    average = multiplied_lst[-1] / len(lst)

    return f'{average:.3f}'

# Their answer:
def round_to_three_digits(number):
    rounded_number_as_str = str(round(number, 3))
    decimal_position = rounded_number_as_str.find('.')

    while len(rounded_number_as_str) - decimal_position < 4:
        rounded_number_as_str += '0'

    return rounded_number_as_str

def multiplicative_average(numbers):
    product = 1

    for num in numbers:
        product *= num

    return round_to_three_digits(product / len(numbers))
   


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")