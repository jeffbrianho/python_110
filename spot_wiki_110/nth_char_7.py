# Write a function that takes a list of words and constructs a new word by
# concatenating the nth letter from each word, where n is the position of the
# word in the list.

# Example:

def nth_char(word_lst):
    final_word = ''
    for index, word in enumerate(word_lst):
        final_word += word[index]

    return final_word


print(nth_char(['yoda', 'best', 'has'])) # should return 'yes'