# Write a function that generates text following a pattern where:
# 1) the first and last characters of each word remain in their original place
# 2) characters between the first and last characters are sorted alphabetically
# 3) punctuation should remain at the same place as it started


"""
chop first and last letter using slicing
use left over mid word and iterate each char if non alpha store index, list new word , sort index punct, join; for punctuation; if
return first and end to middle
"""
def scramble_words(string):
    list_of_words = string.split()
    final_word_list = []

    for word in list_of_words:

        no_punct_word = ''
        saved_punct = []
        for index, char in enumerate(word):
            if char.isalpha():
                no_punct_word += char
            else:
                saved_punct.append((index, char))

        first_letter = no_punct_word[0]
        mid_letters = no_punct_word[1:len(no_punct_word) - 1]
        last_letter = no_punct_word[-1]

        

        sorted_lst_of_chars = (sorted(list(mid_letters)))
        final_mid = ''.join(sorted_lst_of_chars)
                            
        combined_word_no_punct = (first_letter + final_mid + last_letter)
        lsted_final = list(combined_word_no_punct)

        if saved_punct:
            lsted_final.insert(*saved_punct[0])

        final_word = ''.join(lsted_final)
        
        final_word_list.append((final_word))
    return ' '.join(final_word_list)

# Examples:
# print(scramble_words('professionals') == 'paefilnoorsss')
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, " \
"sing like there's nobody listening, and live like it's heaven on earth.") == "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")