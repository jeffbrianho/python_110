# Create a function that takes a string argument and returns the character that 
# occurs most often in the string. If there are multiple characters with the same greatest frequency, 
# return the one that appears first in the string. When counting characters, consider uppercase and 
# lowercase versions to be the same.

"""
P:
I: STRING
O: STRING CHAR
E: case insensitive: return the first one
I

E
D: dictionary char and count method

A:

change word to lower. 
create dictionary of char: char count
make key value to return value
return max by value should return first one
return 


"""

def most_common_char(string):
    lowered_string = string.lower()

    char_count_dict = {char: lowered_string.count(char)
                        for char in lowered_string}
    
    def key_return_value(key):
        return char_count_dict[key]

    return max(char_count_dict, key=key_return_value)

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')


# 7:03 mins ; max returns first max one luckily ***
