# Create a function that takes a string argument and returns the character that occurs most 
# often in the string. If there are multiple characters with the same greatest frequency,
#  return the one that appears first in the string. When counting characters, consider 
# uppercase and lowercase versions to be the same.

"""
P
I:string
O: char
E: return the one with the greatest frequency use the one that appears first:
I: upper and lower are the same return lower

E
D
A: consider a dictionary?
and do the same key thing as problem 4 


"""

def most_common_char(sentence):
    lowered_string = sentence.lower()

    char_dict =  {char: lowered_string.count(char) for char in lowered_string}

    def key_sort_value(dictionary):
        return dictionary[1]
    
    return max(char_dict.items(), key=key_sort_value)[0]

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

# 6 mins
# main thing is sorting by value!