# Write a function that takes a string as an argument and returns that string with every occurrence 
# of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
# 'nine' -- converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.

"""
can use the dict method get. 
"""

def word_to_digit(message):
    NUM_DICT = {
        'one': '1', 
        'two': '2',
        'three': '3',
        'four': '4', 
        'five': '5', 
    }

    return ' '.join([NUM_DICT.get(word, word) for word in message.split()])

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

# took 4:55 mins