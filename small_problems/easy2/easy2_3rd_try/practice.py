# We're receiving a set of messages in code. The messages are sets of text strings, like:
# "alakwnwenvocxzZjsf"
# Write a method to decode these strings into numbers. The decoded number should be the number of 
# lowercase characters between the first two uppercase characters. If there aren't two uppercase characters, 
# the number should be 0.

"""
P
i: List of strings
O: list of numbers
E: the number of lower case between two uppercase
I
empty is empty 

E

D: counter to add to list

A:
Iterate through each word in list
    - for word in list
Iterate through each char in word - helper function 
    - for char in word
Determine if upper and count the number of lower between them - helper function
    `start_count` = False
    count = 0 

    when word indx = .isupper() and toggle off
        start count - turn on
    while toggle is on, and char is lower
        - count+= 1
    if toggle is on and char is upper
        - return count
    else 0
    return a count and append to list
return the count of each word in a list 

"""

def decode(string_list):

    def return_word_count(word):
        start_count = False
        count = 0

        for char in word:
            if char.isupper() and start_count == False:
                start_count = True
            elif char.islower() and start_count == True:
                count += 1
            elif char.isupper() and start_count == True:
                return count
            
        return 0
    
    return [return_word_count(word) for word in string_list]
        
    
    

print(decode(['ZoL', 'heLlo', 'XX']) == [1, 0, 0])
print(decode(['foUrsCoreAnd', 'seven', '']) == [2, 0, 0])
print(decode(['lucYintheskyWith', 'dIaMonDs']) == [8, 1])
print(decode([]) == [])
