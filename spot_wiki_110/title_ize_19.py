# A string is considered to be in title case if each word in the string is either:
# a) Capitalized (that is, only the first letter of the word is in upper case)
# b) Considered to be an exception and put entirely into lower case unless it is
#  the first word, which is always capitalized.

# Write a function that will convert a string into title case, given an optional list
#  of exceptions (minor words). The list of minor words will be given as a string with 
# each word separated by a space. Your function should ignore the case of the minor words 
# string -- it should behave in the same way even if the case of the minor word string is changed.

"""
can make it a comprehension:
cane make each into a list of words
return capitalize() word if word not in casefold str2

"""

def title_case(sentence, sub_sentence=''):
    word_list = sentence.split()
    sub_list = [word.casefold() for word in sub_sentence.split()]
    
    final_list = [word.capitalize()
                                    if word.casefold() not in sub_list 
                                    or word is word_list[0] else
                                    word.lower() 
                                    for word in word_list]
    return ' '.join(final_list)
# Examples:
print(title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings')
print(title_case('THE WIND IN THE WILLOWS', 'The In')  == 'The Wind in the Willows')
print(title_case('the quick brown fox')  == 'The Quick Brown Fox')