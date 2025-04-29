# Write a function to determine if two words are anagrams of each other.

def is_anagram(word1, word2):
   
    def make_dict_char_count(word):                      # tally chars in each word in dict
        return  {char: word.lower().count(char) for char in word.lower() }

    dict1 = make_dict_char_count(word1)
    dict2 = make_dict_char_count(word2)

    return dict1 == dict2

print(is_anagram('Creative', 'Reactive') == True)
print(is_anagram("foefet", "toffee") == True)
print(is_anagram("Buckethead", "DeathCubeK") == True)
print(is_anagram("Twoo", "WooT") == True)
print(is_anagram("dumble", "bumble") == False)