# Your task is to Reverse and Combine Words.
# Input: String containing different "words" separated by spaces
# 1. More than one word? Reverse each word and combine first with second, third with fourth and so on...
# (odd number of words => last one stays alone, but has to be reversed too)
# 2. Start it again until there's only one word without spaces
# 3. Return your result…

"""
P:
I: String of words (sep by space)
O: string of word reversed
E: if more than 1 word, reverse each word and combine 1-2 3-4 4-5 6 until there is only 1 word.
word is char sep by space 
I: alphas and nums

E:  # 1 cbafed only 1x due to 2 letters
    # 2 iterated 2x due to 4 word   cbafed ihglkj 
                                    defabcjklghi

D: lists of separated word
list of combined words

A:
taking each word and reversing them, then combining in pairs
keep reversing and combining until only 1 word (while statement)

while statement len words > 1
break down sentence into individual list of words
reverse word and combine return to `new_list`
use length to combine only 1 and 2 3 and 4 if odd keep last same. consider slicing indexed words

return list as wordlist[0]


"""
def rev_and_combo(word1, word2):
    return (word1[::-1] + word2[::-1])

def reverse_and_combine_text(sentence):
    word_list = sentence.split()

    while len(word_list) > 1:
        changed_list = []

        if len(word_list) % 2 == 0:
            for indx in range(0, len(word_list), 2):
                new_word = rev_and_combo(word_list[indx], word_list[indx + 1])
                changed_list.append(new_word)
        

        else:
            rev_last_word = word_list.pop()[::-1]
            for indx in range(0, len(word_list), 2):
                new_word = rev_and_combo(word_list[indx], word_list[indx + 1])
                changed_list.append(new_word)
            changed_list.append(rev_last_word)

        word_list = changed_list
    return word_list[0]

print(reverse_and_combine_text("abc def")  == "cbafed")
print(reverse_and_combine_text("abc def ghi jkl") == "defabcjklghi")
print(reverse_and_combine_text("dfghrtcbafed") == "dfghrtcbafed")
print(reverse_and_combine_text("234hh54 53455 sdfqwzrt rtteetrt hjhjh lllll12 44") ==
"trzwqfdstrteettr45hh4325543544hjhjh21lllll")
print(reverse_and_combine_text("sdfsdf wee sdffg 342234 ftt") == "gffds432243fdsfdseewttf")

# Time to complete: 37:35 mins
# Theme: manipulate words and return new word in loop for conditional
# Approach: create while loop for condition, use a helper function for concrete actions
# iterate through indexs to work with word pairs. 