# Given a string and an integer i, write a method that splits the string up into a sentence of strings, 
# where each string in the sentence contains a character of the argued string and every ith character after it:

"""
P
I: string, i
O: string
E: splits into the sentence with every ith char after it
I

E

D

A:

make word one word

helper function to create each word
    - takes string and appends every ith to a string
    - return that string

iterate through the condensed string with index increasing until end using helper function
store the word to a list

' ' join list and return 

"""
def fragment(string, i):
    string_condensed = ''.join(string.split())

    def create_word(string, i):
        final_word = ''
        for indx in range(0, len(string), i):
            final_word += string[indx]
        
        return final_word
    
    final_list = []

    if i == 0:
        return "i cannot be less than 1"
    
    for index in range(len(string_condensed)):
        final_list.append(create_word(string_condensed[index:], i))

    return ' '.join(final_list)

# # PYTHON
print(fragment("abcde", 1) == "abcde bcde cde de e")
print(fragment("a b c d e", 2) == "ace bd ce d e")
print(fragment("mary had a little lamb", 3) == "mydila ahatem raltlb ydila hatem altlb dila atem ltlb ila tem tlb la em lb a m b")
print(fragment("abcde", 0) == "i cannot be less than 1")
print(fragment("abcde", 100) == "a b c d e")
print(fragment("", 1) == "")









# Removing Extra Vowels
# Given a word, return a copy of that word, removing every vowel after the first three:

# TEST CASES
# JAVASCRIPT
# console.log(three_vowels("tropical") === "tropical");
# console.log(three_vowels("tropicalia") === "tropical");
# console.log(three_vowels("BliMp123") === "BliMp123");
# console.log(three_vowels("eyelash2!!!") === "eyelsh2!!!");

# PYTHON
# print(three_vowels("tropical") == "tropical")
# print(three_vowels("tropicalia") == "tropical")
# print(three_vowels("BliMp123") == "BliMp123")
# print(three_vowels("eyelash2!!!") == "eyelsh2!!!")