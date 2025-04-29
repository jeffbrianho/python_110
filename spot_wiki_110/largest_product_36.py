# Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits 
# in the given string of digits.

"""
P
I: string of digits
O: product of largest 5 consecutive digits. as an int
E: only digits
I

E: 39583 = 3 * 9 * 5 * 8 * 3
D: list
A:
create a list of all consecutive numbers up to 5 digits
iterate through indx to indx + 5
store in list

separate all digits and turn to num
mulitply the whole thing
store in a list return the largest number



"""

def greatest_product(string_digit):

    def create_5_digit_list(string_num):
        digit_list = []
        for indx in range(len(string_num)):
            digit_list.append(string_num[indx: indx + 5])

        return digit_list
    
    five_digit_list = [(digit) for digit in create_5_digit_list(string_digit)
                                                if len(digit) == 5]
    
    product_list = []
    for s_digit in five_digit_list:
       
        split_digit = list(s_digit)

        count = 1
        for digit in split_digit:
            count *= int(digit)
        product_list.append(count)
    
    
         
    
    max_number = max(product_list)

    return max_number



print(greatest_product("123834539327238239583") == 3240)
print(greatest_product("395831238345393272382") == 3240)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("02494037820244202221011110532909999") == 0)