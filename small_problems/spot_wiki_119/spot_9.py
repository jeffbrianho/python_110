# DONE BUT TOUGH, SHOULD WRITE PEDAC 23:09


# Write a function that generates text following a pattern where:
# 1) the first and last characters of each word remain in their original place
# 2) characters between the first and last characters are sorted alphabetically
# 3) punctuation should remain at the same place as it started

def scramble_words(string):
    string = string.split()
    
    def word_scamble(word):
        cleaned_word = ''
        puncts = []
        for indx, char in enumerate(word):
            if char.isalpha():
                cleaned_word += char
            else:
                puncts.append((indx, char))
        
        new_word_list = [cleaned_word[0]]
        new_word_list.extend((sorted(cleaned_word[1:len(cleaned_word) - 1])))
        new_word_list.append(cleaned_word[-1])

        for punt in puncts:
            (new_word_list.insert(punt[0], punt[1]))
        
        return ''.join(new_word_list)


        
    final_word = []
    for word in string:
        final_word.append(word_scamble(word))

    return ' '.join(final_word)



# Examples:
print(scramble_words('professionals') == 'paefilnoorsss')
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth.") == \
"you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")