# Write a function that, given a string of text, returns a list of the top-3 most
# occurring words, in descending order of the number of occurrences.

# Assumptions:
# - A word is a string of letters (A to Z) optionally containing one or more apostrophes (').
# - Matches should be case-insensitive.
# - Ties may be broken arbitrarily.
# - If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty list if a text contains no words.



def top_3_words(string):
    words_list = string.split()

    def count_method(element): # need to just be 1 element change at a time. 
        return words_list.count(element)

    sorted_words = sorted(words_list, key=count_method, reverse=True)
    key_ordered_dict = {key: sorted_words.count(key) for key in sorted_words}
    key_ordered_list = [key for key in key_ordered_dict
                        if key.isalpha()]
    return key_ordered_list[:3]

# print(count_method(['a', 'a', 'a', 'boy', 'cat', 'cat']))
print(top_3_words('a a a boy cat cat'))
# # Examples:
print(top_3_words(" , e .. ") ==  ["e"])
print(top_3_words(" ... ") == [])
print(top_3_words(" ' ") == [])
print(top_3_words(" ''' ") == [])
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.""") == ["a", "of", "on"])
