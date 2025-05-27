# Create a function that takes a list of integers as an argument. 
# The function should determine the minimum integer value that can be appended to 
# the list so the sum of all the elements equal the closest prime number that is greater 
# than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. 
# The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

# Notes:

# The list will always contain at least 2 integers.
# All values in the list must be positive (> 0).
# There may be multiple occurrences of the various numbers in the list.

"""
P
I: lst
O: int
E: int will be the min int to make the sum to closest prime number graeter than the sum 
I:


E
D
A
: create a sum of the numbers. add from a while loop while sum % (range num) != 0
create an isprime function 
"""

def nearest_prime_sum(lst):

    def is_prime(num):
        return all([num % div != 0 for div in range(2, num)])
    
    def sum_of_lst(lst_of_num):
        return sum(lst_of_num)
    
    starting_num = sum_of_lst(lst)
    num_to_prime = 0
    
    while not is_prime(starting_num) or starting_num == sum_of_lst(lst):
        starting_num += 1
        num_to_prime += 1

    return num_to_prime

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

# 10 mins


def is_prime(num):
    if num <= 1:
        return False
    return all([num % div != 0 for div in range(2, int(num**0.5)) + 1])