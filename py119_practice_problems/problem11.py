# Create a function that takes a nonempty string as an argument and returns a tuple consisting 
# of a string and an integer. If we call the string argument s, the string component of the 
# returned tuple t, and the integer component of the tuple k, then s, t, and k must be related to 
# each other such that s == t * k. The values of t and k should be the shortest possible substring 
# and the largest possible repeat count that satisfies this equation.

# You may assume that the string argument consists entirely of lowercase alphabetic letters.

"""
create a substring that has a multiplier that will equal the length of the string
string length / substring length 9/ x = k
return a substring if substring * k equals the string

"""

def repeated_substring(string):

    def all_substrings(string):
        return [string[:start + 1] for start in range(len(string))]
    
    def constant(string, substring):
        return len(string) // len(substring)
    
    return [(substring, constant(string, substring)) for substring in all_substrings(string)
            if substring * constant(string, substring) == string][0]

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))