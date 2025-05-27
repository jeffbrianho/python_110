# Given a string and an integer i, write a method that splits the string up into a
#  sentence of strings, where each string in the sentence contains a character of the 
# argued string and every ith character after it:

"""
P:
I: string, integer
O: string
E
I

E
D
A


"""


# PYTHON
# print(fragment("abcde", 1) == "abcde bcde cde de e")
# print(fragment("a b c d e", 2) == "ace bd ce d e")
# print(fragment("mary had a little lamb", 3) == "mydila ahatem raltlb ydila hatem altlb dila atem ltlb ila tem tlb la em lb a m b")
# print(fragment("abcde", 0) == "i cannot be less than 1")
# print(fragment("abcde", 100) == "a b c d e")
# print(fragment("", 1) == "")


# Given a string and an integer i, write a method that splits the string up into a sentence of strings, where each string in the sentence contains a character of the argued string and every ith character after it:

"""
P:
I: string, integer i
O: string
E: each string has a char and every iTH char after
I: empty string ==> empty string
only counting the char from that index + the num (i)

E:

D
range (,, i ) for stepping through each char index
list - to hold each word and then join at end
A:
if empty
return string

words_list = []
joining the words to 1 string
start at first index and concatenate at every iTH step range()
take word - append a list
return ' ' .join list 

C

"""

def fragment(sentence, i):

    if not sentence:
        return sentence
    
    if i == 0:
        return "i cannot be less than 1"
    
    word_list = ''.join(sentence.split())

    final_list = []
    
    def make_word(word):
        single_word_list = ''
        for indx in range(0, len(word), i):
            
            single_word_list += word[indx]

        return single_word_list

    for indx in range(len(word_list)):
        final_list.append(make_word(word_list[indx:]))

    

        

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