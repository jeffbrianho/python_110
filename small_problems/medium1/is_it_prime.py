# A prime number is a positive number that is evenly divisible only by itself and 1.
#  Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not prime since 
# it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the number 1 is not prime.

# Write a function that takes a positive integer as an argument and returns true if the number is prime,
#  false if it is not prime.

# You may not use any of Python's add-on packages to solve this problem. Your task is to programmatically 
# determine whether a number is prime without relying on functions that already do that for you.


"""
P:
I: integer
O: boolean
E: only use true or false if prime or not prime

I: whole numbers

E
D
A: this is math: use % conditionals if num / range of nums not including 1 or itself then prime, else false

if num % range 0 - num != 0 
[num == 0]
"""

# def is_prime(num):
#     if num == 1:
#         return False
#     else:
#         divisor_lst = [div for div in (range(1, num + 1)) if num % div == 0]
#         divisor_lst.remove(1)
#         if divisor_lst:
#             divisor_lst.remove(num)
#             if divisor_lst:
#                 return False
#         return True

def is_prime(num):
    if num <= 1:
        return False
    return ([num % div != 0 for div in range(2, int(num**0.5) + 1)])


print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5))# == True)               # True
# print(is_prime(6) == False)              # True
# print(is_prime(7) == True)               # True
# print(is_prime(8) == False)              # True
# print(is_prime(9) == False)              # True
# print(is_prime(10) == False)             # True
# print(is_prime(23) == True)              # True
# print(is_prime(24)== False)             # True
# print(is_prime(997) == True)             # True
# print(is_prime(998) == False)            # True
# print(is_prime(3_297_061) == True)       # True
# print(is_prime(23_297_061) == False)     # True


# second try rote memory 
def is_prime(num):
    if num <= 1:
        return False
    return all([num % div != 0 for div in range(2, int(num**0.5) + 1)])