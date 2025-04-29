# Write a function that takes a string as an argument and returns that 
# string with every occurrence of a "number word" -- 'zero', 'one', 'two', 
# 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

# You may assume that the string does not contain any punctuation.

"""
i: string
o: 

"""

import string
print(string.punctuation)



def word_to_digit(sentence):
    final_sentence = []

    word_list = sentence.split()
    print(word_list)
    for word in word_list:
        match word:
            case 'zero':
                final_sentence.append('0')
            case 'one':
                final_sentence.append('1')
            case 'two':
                final_sentence.append('2')
            case 'three':
                final_sentence.append('3')
            case 'four':
                final_sentence.append('4')
            case 'five':
                final_sentence.append('5')
            case 'six':
                final_sentence.append('6')
            case 'seven':
                final_sentence.append('7')
            case 'eight':
                final_sentence.append('8')
            case 'nine':
                final_sentence.append('9')
            case _:
                final_sentence.append(word)

    return (' ').join(final_sentence)

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message))# == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message))# == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True

NUM_WORDS = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

def word_to_digit(sentence):
    words = sentence.split()
    processed_words = [NUM_WORDS.get(word, word) for word in words]
    return ' '.join(processed_words)

#Use a dictionary to store numbers and use key access to get the desired word. 
# make a list and join using the word as the default if not in the dictionary. 
