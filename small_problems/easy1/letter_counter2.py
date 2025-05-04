# Modify the word_sizes function from the previous exercise to exclude non-letters when determining 
# word size. For instance, the word size of "it's" is 3, not 4.



def word_sizes(s):
    final_dict = {}
          
    word_list = s.split(" ")
    new_word_list = []  

    for word in word_list:
        new_word = ''
        for char in word:
            if char.isalnum():
                new_word += char
        new_word_list.append(new_word)    

    if s == '':
        return {}
    else:
        for word in new_word_list:
            final_dict[len(word)] = final_dict.get(len(word), 0) + 1

    return final_dict




# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})



def clean_up_word(word):
    cleaned_word = ''

    for char in word:
        if char.isalpha():
            cleaned_word += char

    return cleaned_word

def word_sizes(string):
    if string:
        word_list = string.split()
        cleaned_word_list = [clean_up_word(word) for word in word_list]
        word_list_as_len = [len(word) for word in cleaned_word_list]
        return {length: word_list_as_len.count(length) for length in word_list_as_len}
    else:
        return {}

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

#use helper function to make a cleaned word to iterate through