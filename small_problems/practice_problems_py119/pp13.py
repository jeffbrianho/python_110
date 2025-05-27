# Create a function that takes two strings as arguments and returns True if 
# some portion of the characters in the first string can be rearranged to match 
# the characters in the second. Otherwise, the function should return False.

# You may assume that both string arguments only contain lowercase alphabetic characters.
#  Neither string will be empty.

"""
P:
I: string, string2
O:  Boolean
E: if string1 can make string2
all lower no empties
I

E:
D: dictionary/count - compare counts if 2 has at <= amount in dict 1
A:
create dictioanry counts for 1 and two
iterate through 2 and compare membership of values of 2 to 1
if number 2 > number 1 return False


"""

def unscramble(s1, s2):
    d1 = {char: s1.count(char) for char in s1}
    d2 = {char: s2.count(char) for char in s2}

    for key in d2:
        if d2[key] > d1.get(key, 0):
            return False
    
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)

# 6:09 seconds use of get method to check memberhip else 0 and False