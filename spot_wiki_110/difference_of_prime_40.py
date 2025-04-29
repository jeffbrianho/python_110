# Given a List [] of n integers, find the minimum number to be inserted
# in the list, so that the sum of all elements of the list should
# equal the closest prime number.

"""
a prime number is one that is only divisble by itself or 1
if 2, 3, 5, 7, 11
if [num % range of nums (2, num**.5) == 0 

make is prime function

"""
def is_prime(num): 
    return not any([(num % div == 0) for div in range(2, (num // 2) + 1)])


def minimum_number(lst_of_int):
    sum_of_list = sum(lst_of_int)
    counter = 0

    if is_prime(sum_of_list):
        return counter
    
    else:
        while not is_prime(sum_of_list):
            sum_of_list += 1
            counter += 1

        return counter

print(minimum_number([3,1,2]) == 1)
print(minimum_number([5,2]) == 0)
print(minimum_number([1,1,1]) == 0)
print(minimum_number([2,12,8,4,6]) == 5)
print(minimum_number([50,39,49,6,17,28]) == 2)

# 18:47 mins
