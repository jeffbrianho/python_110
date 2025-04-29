# Write a function that takes in a string of one or more words and returns the same string, 
# but with all words of five or more letters reversed. Strings passed in will consist of only
# letters and spaces. Spaces will be included only when more than one word is present.

def spin_words(sentence):
    list_of_words = sentence.split()
    mod_list_of_words = [word if len(word) < 5 else word[::-1] for word in list_of_words
                         ]
    return ' ' .join(mod_list_of_words)


# Examples:
print(spin_words("Hey fellow warriors") == "Hey wollef sroirraw")
print(spin_words("This is a test")  == "This is a test")
print(spin_words("This is another test") == "This is rehtona test")
