"""
PROBLEM:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.
"""

def change_me(sentence):
    sent_list = sentence.split()
    result = []
    for word in sent_list:
        if word == word[::-1]:
            result.append((word.upper()))
        else:
            result.append(word)
    final_result = ' '.join(result)
    return final_result

print(change_me("We will meet at noon")    ==    "We will meet at NOON")
print(change_me("No palindromes here")    ==    "No palindromes here")
print(change_me("")                         == "")
print(change_me("I LOVE mom and dad equally") =="I LOVE MOM and DAD equally")