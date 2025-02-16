# Given a string of words separated by spaces, write a function that swaps the first 
# and last letters of every word.

# You may assume that every word contains at least one letter, and that the string 
# will always contain at least one word. You may also assume that each string contains
#  nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.


"""
P:
INPUT string separated by spaces
OUTPUT function that swaps first and last letter of each word (string)
EXPLICIT: string only has letters no repeated spaces will always cotain a word
IMPLICIT
QUESTIONS

E 
D:
list
string

A
separate each word 
swap each letter
rejoin each word into a sentence
return word

"""

def swap(s):
    string_list = s.split(' ')
    
    new_string_list = []
    
    for word in string_list:
        if len(word) > 1:
            new_string_list.append(word[-1] + word[1:len(word)-1] + word[0])
        else:
            new_string_list.append(word)

    final_string = ' '.join(new_string_list)
    return final_string

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True