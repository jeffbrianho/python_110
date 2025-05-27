# Write a function that takes a string as an argument and returns that string with a 
# staggered capitalization scheme. Every other character, starting from the first, 
# should be capitalized and should be followed by a lowercase or non-alphabetic character.
#  Non-alphabetic characters should not be changed, but should be counted as characters for
#  determining when to switch between upper and lower case.

"""

P
I String
O string staggard caps every other should be caps followed by lower
don't change non alpha but should be counted when to change
E start with caps
I

E
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

D: strings

A
have empty string
use enumerate to change every other if indx % 0 == 0  every even is caps every odd is lower
return string

"""

def staggered_case(s):
    final_string = ''
    for indx, char in enumerate(s):
        if indx % 2 == 0:
            final_string += char.upper()
        else:
            final_string+= char.lower()
    return final_string

#theirs
def staggered_case(string):
    result = ''
    for idx, char in enumerate(string):
        func = char.upper if idx % 2 == 0 else char.lower # they use a ternary here
        result += func()

    return result

#can we do a comprehension with an if else statement?

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

### second attepts


def staggered_case(string):
    return ''.join([string[indx].upper() 
            if indx % 2 == 0 else string[indx].lower() 
            if string[indx].isalpha() else string[indx]
            for indx in range(len(string))
            ])
