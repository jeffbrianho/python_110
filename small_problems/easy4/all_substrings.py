# Write a function that returns a list of all substrings of a string. 
# Order the returned list by where in the string the substring begins.
#  This means that all substrings that start at index position 0 should come first, 
# then all substrings that start at index position 1, and so on. Since multiple substrings 
# will occur at each position, return the substrings at a given index from shortest to longest.

# You may (and should) use the leading_substrings function you wrote in the previous exercise:


def leading_substrings(s):
    return [s[:indx + 1] for indx in range(len(s))]

def substrings(s):
    count = 0 
    final_list = []
    while count < len(s):
        final_list.extend(leading_substrings(s[count:]))
        count += 1
    return final_list
    

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True


# This will provide a list of all substring iterations in order. 

#second attempt with help 7 mins

def leading_substrings(string):
    return [string[:end + 1] for end in range(len(string))]

def substrings(string):
    return [substring for start in range(len(string))
                      for substring in leading_substrings(string[start:])]
    

