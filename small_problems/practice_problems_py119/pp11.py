# Create a function that takes a nonempty string as an argument and returns a 
# tuple consisting of a string and an integer. If we call the string argument s, 
# the string component of the returned tuple t, and the integer component of the tuple k, 
# then s, t, and k must be related to each other such that s == t * k. The values of t and k 
# should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

# You may assume that the string argument consists entirely of lowercase alphabetic letters.

"""
P
I: string
O: tuple (string, int)
E: s ==> (t, k): s == t * k shortest possible substring and largest k
I

E: xyz 3 times
D: string - we are working with
    string we are using as substring
    integer to determine amount of times sub in string
    tuple to return
A:

find substrings greater than 1
    - do all substrings with if conditional of len>1
if the substring * (len string / len substring) = string keep as tuple (substring, len(String/lensub))
    select from substrings as if conditional:

list of tuples sort by largest [1]

return tuple

"""

def repeated_substring(s):
    length = len(s)

    all_substrings = [s[:start]
                for start in range(len(s) + 1)
                if len(s[:start]) > 0]
    
    comp_sub = [(substring, (length // len(substring))) for substring in all_substrings
        if substring * (length // len(substring)) == s]

    def key_sort(tup):
        return tup[1]
    
    return max(comp_sub, key=key_sort)



print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

# 19:21 mins
