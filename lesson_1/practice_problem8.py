#Given the following string, create a 
# dictionary that represents the 
# frequency with which each letter
#  occurs. The frequency count should
#  be case-sensitive:



"""
P:
input: string
output: dictionary
explicit: keys are the letters, values are occurance
case sensitive
implicit:n/a
questions:n/a

E:
D dicts
A:
create empty dict
loop through each character in the string
create a dict using key/value index assignment
value will be count of  letter in string
output dict
"""

statement = "The Flintstones Rock"

final_dict = {}

for letter in statement:
    if letter.isalnum():
        final_dict[letter] = statement.count(letter)

print(final_dict)

char_freq = {}
statement = statement.replace(' ', '')
for char in statement:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)