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
   


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")