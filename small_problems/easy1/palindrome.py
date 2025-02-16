# Write a function that returns True if the string passed as an argument is a palindrome, 
# False otherwise. A palindrome reads the same forwards and backwards. 
# For this problem, the case matters and all characters matter.

"""
P:
INPUT: String
OUTPUT: Boolean

EXPLICIT: read a string if it "Reads forwards the same as backwards
case matters and characters matter:
IMPLICIT: 

E: 
# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
D: string

A: create a conditional to provide a boolean if its reverse == normal
print boolean

C

"""



def is_palindrome(string):
    return(string == string[::-1])


# # All of these examples should print True

# print(is_palindrome('madam') == True)
# print(is_palindrome('356653') == True)
# print(is_palindrome('356635') == False)

# # case matters
# print(is_palindrome('Madam') == False)

# # all characters matter
# print(is_palindrome("madam i'm adam") == False)