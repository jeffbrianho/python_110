# Create a function that takes a string of digits as an argument and 
# returns the number of even-numbered substrings that can be formed. For example,
#  in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', 
# for a total of 6 substrings.

# If a substring occurs more than once, you should count each occurrence as a separate substring.
"""
P
i: string of digits
o: int
e: the number of even numbered substrinsg that can be formed
count all the substrings
i

E: 1432 - 14, 4, 432, 32, 2, 1432
D: list of substrings
int coersion
A:
create a list of all substrings but select for int(sub) % 2 == 0
return length

"""

def even_substrings(digit_string):
    all_substrings = [digit_string[start:end]
                for start in range(len(digit_string))
                for end in range(start + 1, len(digit_string) + 1)]

    even_subs = [even_sub for even_sub in all_substrings
                if int(even_sub) % 2 == 0]

    return len(even_subs)



print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

# 6:38 mins - use of substrings and a selection 