# Some numbers have funny properties. For example:
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given a positive integer n written as abcd... (a, b, c, d... being digits)
# and a positive integer p we want to find a positive integer k, if it exists,
# such as the sum of the digits of n taken to the successive powers of p is
# equal to k * n.
# In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...)
# = n * k
# If it is the case we will return k, if not return -1.
# Note: n and p will always be given as strictly positive integers.

"""
P
I: n, p
O: k
E: 4^3 6^4 2^ 5 8^6 8^7 = num 
num / n = k if num%n == 0 

else return -1
I

E
D: string to break down numbers
list to create a sum or iterable for p range

A:
break down the number to get the sum of each number to the p power. and sum
create conditionatl if num % orginal n == 0. return num/n else return -1

"""
def break_down_num(num, power):
    num_list = [int(num) for num in str(num)]
    progressing_power = power

    final_sum = 0 
    for num in num_list:
        final_sum += num**progressing_power
        progressing_power += 1
    
    return final_sum

def dig_pow(n, p):
    num = break_down_num(n, p)
    if num % n == 0:
        return num // n
    else:
        return -1 

print(dig_pow(89, 1) == 1)
print(dig_pow(92, 1) == -1)
print(dig_pow(46288, 3) == 51)
print(dig_pow(695, 2) == 2)

# Time to complete: 16:53 mins
# Theme: Math related with advancing powers
# Approach: dissecting numbers by using string function. conditional statements. 
