# Write a function that takes a string, doubles every character in the string, 
# then returns the result as a new string.



"""
P
I: STRING
O: STRING 
E: EACH CHAR DOUBLED
I
E
D
A

use * to double

"""

def repeater(s):
    final_s = ''
    for char in s:
        final_s += char * 2
    
    return final_s


print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True


#Their answer
def repeater(string):
    return ''.join([char * 2 for char in string])

#myanswer
def repeater(string):
    return ''.join([char * 2 for char in string])