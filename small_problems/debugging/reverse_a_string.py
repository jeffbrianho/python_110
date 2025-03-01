# You have a function that is supposed to reverse a 
# string passed as an argument. However,
#  it's not producing the expected output. Explain the bug, and provide a solution.

def reverse_string(string):
    rev_string = ''
    for char in string:
        rev_string = char + rev_string

    return rev_string

# string = ollehhello
# it is adding to the original string. must delete the original before overriding
print(reverse_string("hello") == "olleh")