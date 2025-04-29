# Write a function that finds all the anagrams of a word from a list.
# Two words are anagrams of each other if they both contain the same letters.

# Examples
# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false

def create_dict(string):
    lst_of_char = list(string)

    dict_of_char_and_freq = {char: string.count(char) for char in lst_of_char}

    return dict_of_char_and_freq

def anagrams(string, lst):
    reference_dict = create_dict(string)

    final_lst = [anagram for anagram in lst
                 if create_dict(anagram) == reference_dict]
    
    return final_lst

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer'])
print(anagrams('laser', ['lazing', 'lazy', 'lacer']) == [])



# Shelbys way 
def anagrams(string_arg, lst):

    anagrams_list = []

    for string in lst:
        if sorted(string) == sorted(string_arg): #Such a simple solution! Think: Anagrams are just unsorted strings! So SORT THEM!
            anagrams_list.append(string)

    return anagrams_list
