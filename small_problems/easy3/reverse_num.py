# Write a function that takes a positive integer as an argument and returns that 
# number with its digits reversed.

"""
p
i int
o int reverse
e only numbers if preceeding 0 only whole numb
i

e
d
a change from int to str use reverse method change back to int






"""


def reverse_number(num):
    reversed_string_num = (str(num))[::-1]
    final = int(reversed_string_num)
    return final
    
#Their answer
def reverse_number(number):
    return int(str(number)[::-1])

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True