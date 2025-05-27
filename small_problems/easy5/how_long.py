# Write a function that takes a string as an argument and returns a 
# list that contains every word from the string, with each word followed 
# by a space and the word's length. If the argument is an empty string or if 
# no argument is passed, the function should return an empty list.

# You may assume that every pair of words in the string will be separated by a single space.

"""
P:
i: string
o: list containing every word from the string followed by space and length of word
empty string or no argument is an empty list
e
i
E
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

D: list, string
A:
create empty final list
create string_list using split() should make list of words (may need conditional for empty)
iterate through string list and append string and len string to final list
return final list

"""

def word_lengths(string=''):
    if not string:
        return []

    else:
        final_list = [f'{word} {len(word)}' for word in string.split(' ')]
        return final_list



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




# MAIN TAKEAWAY IS USING (string='') as a default parameter for empty arguments

# second attempt 1 min

def word_lengths(strings=''):
    return [f'{string} {len(string)}' for string in strings.split()]
