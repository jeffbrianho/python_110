# Write a function that takes a string as an argument and returns a list that contains every word from the
#  string, with each word followed by a space and the word's length. If the argument is an empty string or 
# if no argument is passed, the function should return an empty list.

# You may assume that every pair of words in the string will be separated by a single space.

"""
P:
I: string
O: list
E: each word followed by a space and word length; empty list if other
I: make sure to make default value

E:
D: list
string
f strings
A:

separate each word by a space.
iterate through list of words
return an f string of the word and the len of word
can use a comprehension 


"""

def word_lengths(words=''):
    
    return [f'{word} {len(word)}' for word in words.split()]

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True

# 5:12 mins did full pedac and check for examples 