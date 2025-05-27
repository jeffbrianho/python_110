# Write a function that returns a list of all substrings of a string. Order the returned list 
# by where in the string the substring begins. This means that all substrings that start at 
# index position 0 should come first, then all substrings that start at index position 1, and so on. 
# Since multiple substrings will occur at each position, return the substrings at a given index from
#  shortest to longest.

# You may (and should) use the leading_substrings function you wrote in the previous exercise:

"""
input string
outputlist of all substrings
goes from 0:1 - end then 1:2 - end
for start in range len(0 to end)
    to end in range start, len + 1



"""

def substrings(string):
    return [string[start:end] for start in range(len(string))
                            for end in range(start + 1, len(string) + 1)]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

# commited to memory but understand the mechanics. 
# start is 0, 1, 2, 3, 4
# end is 1, 2, 3, 4, 5 ==> 0:1, 0:2, 0:3, 0:4, 0:5, 1:2, 1:3, 1:4, 1:5, 2:3, 2:4, 2:5, 3:4, 3:5, 4:5, 