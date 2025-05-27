# Create a function that takes a string as an argument and returns True if the string is a pangram, 
# False if it is not.

# Pangrams are sentences that contain every letter of the alphabet at least once. 
# For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses
#  every letter at least once. Note that case is irrelevant.


"""
P
I: string
O: Boolean
E: pangram contain every letter of the alphabet at least once
I: can use membership

E
D: list of chars

A:
create a list of chars and check to see if letter is in string.casefoold
return False if not

"""

def is_pangram(s):

    ALPHA_LIST = 'abcdefghijklmnopqrstuvwxyz'

    for char in ALPHA_LIST:
        if char not in s:
            return False

    return True

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

# 4:28 mins membership of alphabet