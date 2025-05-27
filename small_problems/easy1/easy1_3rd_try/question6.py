# Modify the word_sizes function from the previous exercise to exclude non-letters when 
# determining word size. For instance, the word size of "it's" is 3, not 4.

def word_sizes(string):
    word_list = string.split()

    length_list = [len(clean_word(word)) for word in word_list]
    
    return {num: length_list.count(num) for num in length_list}

def clean_word(word):
    cleaned_word = ''
    for char in word:
        if char.isalpha():
            cleaned_word += char
    return cleaned_word


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

# spent time troubleshooting due to poor variable wording 2:23 mins make sure to test often
