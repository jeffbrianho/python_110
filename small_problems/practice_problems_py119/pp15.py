# Create a function that takes a string argument that consists entirely of numeric digits 
# and computes the greatest product of four consecutive digits in the string. The argument 
# will always have more than 4 digits.

"""
P
I: string of numerics
O: greatest product of 4 consecutive digits
E: 
I

E
D: list of substrings len 4
iterate and create a product of each

A:
get substrings from start - len of start + 4
if len(substring) == 4

get multiple:
    - iterate through string coercing through int and multipling - make function
    may need to do this with a for loop and counter
        counter = 1
        for num in string 
        counter *= int(num)

make list of multiples and return max num
     max[multiple(substring) for substring in allsubs]


C

"""

def greatest_product(str_num):
    all_subs_4 =    [str_num[start:start + 4] 
                    for start in range(len(str_num))
                    if len(str_num[start:start + 4]) == 4 ]

    def get_multiple(s_num):
        total = 1

        for num in s_num:
            total *= int(num)
        
        return total

    return max([get_multiple(substring) for substring in all_subs_4])

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# 10:22 mins