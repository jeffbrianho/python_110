# Create a function that takes a string of digits as an argument and returns the 
# number of even-numbered substrings that can be formed. For example, in the case of 
# '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

# If a substring occurs more than once, you should count each occurrence as a separate substring.

"""
P
I: string
O: int
E: of even numbered substrings that can be formed in order!
I

E: 
D: list with all substrings; if int%2==0
A


"""

def even_substrings(string):
    return len([string[start:end] for start in range(len(string))
                                for end in range(start + 1, len(string) + 1)
                                if int(string[start:end]) % 2 == 0])

print(even_substrings('1432')  == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)