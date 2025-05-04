# Write a function that takes a string consisting of zero or more space-separated 
# words and returns a dictionary that shows the number of words of different sizes.

# Words consist of any sequence of non-space characters.

"""
P:
INPUT: string of 0 or more space separated words
OUTPUT: dictionary number of words of different sizes
EXPLICIT: Words = non-space chars
IMPLICIT: 
QUESTIONS: size means length of char?

E:
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
D:
dictionary
strings
list of strings
A:
create an empty dict:
separate each word and add to list
go through each word in list for length and create a key with its length
the value should be 0 with a counter +1 if added using .get
return dict

"""

def word_sizes(s):
    final_dict = {}

    word_list = s.split(" ")
    if s == '':
        return {}
    else:
        for word in word_list:
            final_dict[len(word)] = final_dict.get(len(word), 0) + 1

    return final_dict

    
def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        word_size = len(word)
        if word_size not in counts:
            counts[word_size] = 0

        counts[word_size] += 1

    return counts


# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

def word_sizes(string):
    if string:
        word_list = string.split()
        word_list_as_len = [len(word) for word in word_list]
        return {length: word_list_as_len.count(length) for length in word_list_as_len}
    else:
        return {}

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

# 4 mins
# create a dict/count - change words into lengths