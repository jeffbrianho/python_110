
def longest(string):
    list_of_strings = [] 
    final_string = ''
    for char in string: 
        if final_string == '':          # checks to see if string is empty and adds letter to list
            final_string += char 
        elif final_string[-1] <= char:  # checks to see if the last letter in `final_string` is <= next char and adds if True
            final_string += char 
        else:                           # if not <=, it sends that to a list and starts to add the char to the new final string
            list_of_strings.append(final_string)
            final_string = ''
            final_string += char 

    list_of_strings.append(final_string) # if it gets to the end of the iteration, it will add the final value of final_string

    return max(list_of_strings, key=len)

print(longest('asd') == 'as') 
print(longest('nab') == 'ab') # n ab
print(longest('abcdeapbcdef') ==  'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
print(longest('asdfbyfgiklag') == 'fgikl')
print(longest('z') == 'z')
print(longest('zyba') == 'z')