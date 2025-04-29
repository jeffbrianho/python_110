# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols and return the final state of the string.


"""
P
I: string with chars and #
O: new string 
E: # will remove the last letter; consider pop
I: only consecutive letters and chars/#

E 'ac'
D lists to use a pop method
A: 
create a list with all the letters appended if meets # pop
return list

use listed_string = list(string)
final list = 
iterate through listed_string and add to a final_list if char
if # pop final list. 
dont need to worry about starting with #
return final list joined

"""

def clean_string(string):
    listed_string = list(string)
    
    final_string = ''
    final_list = []
    for char in listed_string:
        if char == '#' and final_list:
            final_list.pop()
        else:
            final_list.append(char)
    if final_list:
        final_string += ''.join(final_list)

    return final_string
print(clean_string('abc#d##c') == "ac")
print(clean_string('abc####d##c#') == "")

# 7.41 mins