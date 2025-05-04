# Create a function that takes two string arguments and returns the number of times
# that the second string occurs in the first string. Note that overlapping strings don't
#  count: 'babab' contains 1 instance of 'bab', not 2.

# You may assume that the second argument is never an empty string.

"""
P
I: two strings
O: int
E: output is number of times that string occurs in the first string no empty strings
I

E
D: consider a list to keep the string count and use length 
A
iterate through string and remove substring each time until you cannot while loop
?
string while substing in string.
remove(substring) string
count +1

iterate through substrings while it creates each substring and append when they equal


"""

def count_substrings(string, substring):
    return string.count(substring)


print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)


def count_substring(string, substring):
    count = 0
    i = 0
    while i <= len(string) - len(substring):
        if string[i:i + len(substring)] == substring:
            count += 1
            i += len(substring)  # Move past the found substring (non-overlapping)
        else:
            i += 1
    return count
