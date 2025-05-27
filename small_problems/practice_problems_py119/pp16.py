# Create a function that returns the count of distinct case-insensitive alphabetic characters 
# and numeric digits that occur more than once in the input string. You may assume that 
# the input string contains only alphanumeric characters.

"""
P
I: string
O: int
E: count of distinct case insenstivite alpha and numbers occuring more than one time 
I

E
D
A: make a set reference to iterate through
if the char in set count is > 1 add to count
return count

"""

def distinct_multiples(string):
    single_char = set(string.casefold())

    count = 0
    for char in single_char:
        if string.casefold().count(char) > 1:
            count += 1
    
    return count 


print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# 3:21 mins