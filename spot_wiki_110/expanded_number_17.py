# You will be given a number, and you need to return it as a string in
# expanded form. For example:

def expanded_form(num):
    string_num = str(num)
    length_of_string = len(string_num)
    expanded_num_as_string = ''

    for index, char in enumerate(string_num):
        if char == '0':
            continue
        elif length_of_string != (index + 1):
            expanded_num_as_string += char + ((length_of_string - (index + 1)) * '0') + ' + '
        else:
            expanded_num_as_string += char + ((length_of_string - (index + 1)) * '0')

    return expanded_num_as_string



"""
make into a string
determine length
go by index and add remaining if '0' skip
return string form

"""

print(expanded_form(12) =='10 + 2')
print(expanded_form(42) == '40 + 2')
print(expanded_form(70304) == '70000 + 300 + 4')

# Note: All numbers will be whole numbers greater than 0.