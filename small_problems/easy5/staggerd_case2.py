# Modify the function from the previous exercise so it ignores 
# non-alphabetic characters when determining whether it should 
# uppercase or lowercase each letter. The non-alphabetic characters 
# should still be included in the return value; they just don't count when toggling the desired case.


"""
P:
    I: STRING
    O: STRING
    E: every other caps if char
    I

E:

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

D: string conditionals

A: good case for isalpha() , isupper() functions
can check last in storage list if [-1] is upper, make lower else make upper

final_string
iterate through string by char
    if char isalpha 
        if finalstring[-1] == '' or finalstring[-1]isupper
        add to final string.lower() 
        else add char.upper
    else add char

return final string

"""

def staggered_case(string):
    final_string = ''
    alpha_only_reference = ''

    for char in string:
        if char.isalpha():
            if alpha_only_reference == '' or alpha_only_reference[-1].islower():
                final_string += char.upper()
                alpha_only_reference += char.upper()
            else:
                final_string += char.lower()
                alpha_only_reference += char.lower()
            
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

# required a storage of char to keep track of upper and lower

#their answer

def staggered_case(string):
    result = ''
    upper = True #this is their counter!

    for char in string:
        if char.isalpha(): #deal with only alphas 
            result += char.upper() if upper else char.lower() #if upper is True (make it upper) if not make it lower
            upper = not upper # reverse the trutiness from "not True" to upper = False; then not False to True (switch it)
        else:
            result += char # if it is not a alpha just add it space or num or special char

    return result


# my second ansewr 6 mins
def staggered_case(string):
    upper_toggle = True
    final_string = ''
    
    for char in string:
        if upper_toggle:
            if char.isalpha():
                final_string += char.upper()
                upper_toggle = False
            else:
                final_string += char
        else:
            if char.isalpha():
                final_string += char.lower()
                upper_toggle = True
            else:
                final_string += char

    return final_string

# upper = not upper # reverse the trutiness from "not True" to upper = False; then not False to True (switch it)
# this would be an easier toggle make it not what it was
# pretty close if i had the not upper logic down. 
