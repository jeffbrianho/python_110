# Write a function `generate_hashtag(s)` that generates a hashtag from the given string `s`.

# Rules:
# - The hashtag must start with a '#' symbol.
# - All words in the hashtag must start with a capital letter.
# - If the resulting hashtag is longer than 140 characters, the function should return `False`.
# - If the input string or the resulting hashtag is an empty string, the function should return `False`.

"""
I: String
o: string with # start with capital letters  if len > 140 == False or empty 


A :
start with conditionals if string is empty return False:
can split sentence and return word.capitalize() joined
if len of final word >140 return false else return word
"""

def generate_hashtag(s):
    if s.strip() == '':
        return False
    else:
        final_word_char = [word.capitalize() for word in s.split()]
    
    final_word = '#' + ''.join(final_word_char)
    if len(final_word) > 140:
        return False
    else:
        return final_word

# # Examples:
# print(generate_hashtag("")                       == False)
# print(generate_hashtag(" " * 200)              == False)
# print(generate_hashtag("Do We have A Hashtag")   == "#DoWeHaveAHashtag")
# print(generate_hashtag("Nice To Meet You")       == "#NiceToMeetYou")
# print(generate_hashtag("this is a test")         == "#ThisIsATest")
print(generate_hashtag("this is a very long string" + " " * 140 + "end")  == "#ThisIsAVeryLongStringEnd")
print(generate_hashtag("a" * 139)                == "#A" + "a" * 138)
print(generate_hashtag("a" * 140)                == False)