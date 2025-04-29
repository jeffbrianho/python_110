# Find the highest scoring word in a string.
# Each letter scores points based on its position in the alphabet: a = 1, b = 2, c = 3, ... z = 26.
# Return the highest scoring word. If two words score the same, return the word that appears earliest in the string.

"""
P
I: string ( sentence)
O: highest scoring string based on numberposition in alphabet
E
I

E

D: list or dictionary of letters
list-reference

A: 
create a number reference to add: lists a-z lower
its index can be its worth

split word into list
iterate through each letter and sum
and return as (count, word) tup to list
use max and return tup[1]


"""

def high(sentence):
    ALPHA_REFERENCE = list('_abcdefghijklmnopqrstuvwxyz')

    word_list = sentence.split()
    amount_word_list = []
    for word in word_list:
        amount = 0 
        for char in word:
            amount += ALPHA_REFERENCE.index(char)

        amount_word_list.append((amount, word))

    return max(amount_word_list)[1]

print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')
print(high('aaa b') == 'aaa')