# Write a function that takes a string as an argument and returns that string with a staggered 
# capitalization scheme. Every other character, starting from the first, should be capitalized 
# and should be followed by a lowercase or non-alphabetic character. 
# Non-alphabetic characters should not be changed, but should be counted as characters for
#  determining when to switch between upper and lower case.


"""
I: string
O: case staggered
E: even spaces are pper or lower

iterate through indexes for string[indx] in rangelen string
if indx % 00 upper else lower
potentially join?

can concatenate the string as well 

"""

# def staggered_case(string):
#     return ''.join([string[indx].upper() 
#                      if indx % 2 == 0
#                      else string[indx].lower()
#                      for indx in range(len(string))])

def staggered_case(string):
    final_string = ''

    for indx in range(len(string)):
        if indx % 2 == 0:
            final_string += string[indx].upper()
        else:
            final_string += string[indx].lower()

    return final_string
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

# 6:18 min tried both ways