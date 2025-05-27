# Given a string of words separated by spaces, write a function that swaps the first and last letters 
# of every word.

# You may assume that every word contains at least one letter, and that the string will 
# always contain at least one word. You may also assume that each string contains nothing 
# but words and spaces, and that there are no leading, trailing, or repeated spaces.

"""
sep words
swap words
join words

"""

def swap(sentence):
    word_list = sentence.split()
    
    def swap_word(word):
        if len(word) > 1:
            return word[-1] + word[1:len(word) - 1] + word[0]
        else:
            return word
    
    swapped_list = [swap_word(word) for word in word_list]

    return ' '.join(swapped_list)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

# 4:03 min good job with making sure I print often. use of helper function, short algorithm to make sure i follow steps

