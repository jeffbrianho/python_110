# Create a function that takes a list of integers as an argument and returns the integer 
# that appears an odd number of times. There will always be exactly one such integer in the input list.

"""
P
I: list of integers
O: integer
E: that appears an odd number of times
I

E
D
A
make num count dic
if dic[key] % 2 != 0 return key


"""

def odd_fellow(lst):
    dict_num = {num: lst.count(num) for num in lst}
    
    return [odd for odd in dict_num
            if dict_num[odd] % 2 != 0][0]

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

# 2:42 mins