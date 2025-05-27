# The principal of a school likes to put challenges to the students related with finding words of certain features. One day she said: "Dear students, the challenge for today is to find a word that has only one vowel and seven consonants but cannot have the letters "y" and "m". I'll give a special award for the first student that finds it." One of the students used his dictionary and spent all the night without sleeping, trying in vain to find the word. The next day, the word had not been found yet. This student observed that the principal has a pattern in the features for the wanted words:

# The word should have n vowels, may be repeated, for example: in "engineering", n = 5.

# The word should have m consonants, may be repeated also: in "engineering", m = 6.

# The word should not have some forbidden letters (in an array), forbid_letters

# You will be provided with a list of words, WORD_LIST(python/crystal), wordList(javascript), wordList (haskell), $word_list(ruby), and you have to create the function, wanted_words(), that receives the three arguments in the order given above, wanted_words(n, m, forbid_list)and output an array with the word or an array, having the words in the order given in the pre-loaded list, in the case of two or more words were found.

# Let's see some cases:

# wanted_words(1, 7, ["m", "y"]) == ["strength"]
# wanted_words(3, 7, ["m", "y"]) == ['afterwards', 'background', 'photograph', 'successful', 'understand']
# For cases where no words are found the function will output an empty array.

# wanted_words(3, 7, ["a", "s" , "m", "y"]) == []
# Help our student to win this and the next challenges of the school. He needs to sure about a suspect that he has. That many times there are no solutions for what the principal is asking for. All words have its letters in lowercase format. Enjoy it!




WORD_LIST = ["strength",'afterwards', 'background', 'photograph', 'successful','understand']

def wanted_words(n, m, forbid_let):
    final_list = []
    VOWELS = "aeiou"

    def has_vowels(word):
        count = 0

        for char in word:
            if char in VOWELS:
                count += 1

        return count
    
    def has_consonants(word):
        count = 0

        for char in word:
            if char not in VOWELS:
                count += 1

        return count
    
    def in_list(word):
        return all([char not in forbid_let for char in word])
    
    for word in WORD_LIST:
        if has_vowels(word) == n and has_consonants(word) == m and in_list(word):
            final_list.append(word)
    
    return final_list


print(wanted_words(1, 7, ["m", "y"]) == ["strength"])
print(wanted_words(3, 7, ["m", "y"]) == ['afterwards', 'background', 'photograph', 'successful','understand'])