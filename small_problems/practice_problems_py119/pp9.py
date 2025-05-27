# Create a function that takes two string arguments and returns the number of 
# times that the second string occurs in the first string. Note that overlapping strings 
# don't count: 'babab' contains 1 instance of 'bab', not 2.

# You may assume that the second argument is never an empty string.

"""
P
I: 2 string
O: int
E: number of times that the second string occurs in the first
I:

E:
D: consider use of count?
A:
return the count of substring in string?

iterate through the string, when it encounters the first
letter start range of [0 through length ] if matches add to count and increase indx to new amount

"""

# def count_substrings(s, sub):
#     return s.count(sub)

def count_substrings(s, sub):
    count = 0
    indx = 0

    while indx < len(s):
        if s[indx:indx + len(sub)] == sub:
            count += 1
            indx += len(sub)
            
        else:
            indx += 1

    return count



print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

# 1:55 min 
# can i do this without using a method? yes:
# took a while to get the indxing slice