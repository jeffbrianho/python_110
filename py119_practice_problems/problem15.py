# Create a function that takes a string argument that consists entirely of numeric digits
#  and computes the greatest product of four consecutive digits in the string. 
# The argument will always have more than 4 digits.

"""
P
I: STRING
O: int
E: greatest of 4 consecutive digits
I

E
D
A: create substring of 4:
int and product
product function

"""

def greatest_product(string_num):

    def return_product(lst_of_num):
        a, b, c, d = lst_of_num
        return (a * b * c * d)
    
    def make_string_lst_num(string):
        string_lst = [int(char) for char in string]
        return string_lst
    
    list_of_four = [string_num[start:end] for start in range(len(string_num))
                                    for end in range(start + 1, len(string_num) + 1)
                                    if len(string_num[start:end]) == 4]
    return max([return_product(make_string_lst_num(substring)) for substring in list_of_four])

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# 6:30 mins