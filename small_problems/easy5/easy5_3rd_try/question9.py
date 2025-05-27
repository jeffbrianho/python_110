# Modify the function from the previous exercise so it ignores 
# non-alphabetic characters when determining whether it should uppercase or 
# lowercase each letter. The non-alphabetic characters should still be included in 
# the return value; they just don't count when toggling the desired case.

"""
iterate through each char if char isalpha, change else continue
make a toggle for upper
and whenever doing one make not-upper
upper = not upper

"""

def staggered_case(string):

    final_string = ''
    upper = True

    for char in string:
        if char.isalpha():
            if upper:
                final_string += char.upper()
            else:
                final_string += char.lower()

            upper = not upper
        else:
            final_string += char
    
    return final_string


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True