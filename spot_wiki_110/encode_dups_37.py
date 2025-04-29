# The goal of this exercise is to convert a string to a new string where each character in the new string 
# is "(" if that character appears only once in the original string, or ")" if that character appears 
# more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
"""
P:
I: string
O: new string each char is ( if the char only appears 1x or )
E: ignore caps
I: takes whitespace, and special chars

E
D: dictionary for num?
if key == 1 create a string ( else create )
A
start by make a dict of char to count: this will be our reference
`final_string` = ''
iterate through word chars and reference dict; concatenate a string ( if dictchar = 1 concatenate ) otherwise
return final_string

"""
def duplicate_encode(string):
    string = string.lower()
    dict_reference = {char: string.count(char) for char in string}
    

    final_string = ''
    for chars in string:
        if dict_reference[chars] == 1:
            final_string += '('
        else:
            final_string += ')'
    return final_string

print(duplicate_encode("din") == "(((")
print(duplicate_encode("recede") == "()()()")
print(duplicate_encode("Success") == ")())())")
print(duplicate_encode("(( @") == "))((")

# 10 mins
