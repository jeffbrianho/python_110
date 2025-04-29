# Given two words, determine the number of letters you need to remove from them to make them anagrams.



def anagram_difference(word1, word2):

    def create_list_count(word):
        return [(char, word.count(char)) for char in word]
    
    set1 = set(create_list_count(word1)) 
    set2 = set(create_list_count(word2))

    same_tups = set1.intersection(set2)
    in_set1 = set1.difference(set2)
    in_set2 = set2.difference(set1)

    def make_dict(set_tups):
        return {tup[0]: tup[1] for tup in set_tups}
    
    dict1 = make_dict(in_set1)
    dict2 = make_dict(in_set2)

    count = 0

    if dict1:
        for key in dict1:
            if key in dict2:
                count += abs(dict1[key] - dict2[key])
            else:
                count += dict1[key]
        for key in dict2:
            if key not in dict1:
                count += dict2[key]

    return count
print(anagram_difference('', '') ) #== 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') )# == 1)
print(anagram_difference('ab', 'ba') == 0)
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2)
print(anagram_difference('a', 'aab') == 2)