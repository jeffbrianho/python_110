

def sort_by_consonant_count(lst):

    def count_adj_consonant(word):
        count = 0
        count_storage = []
        indx = 0 
        VOWELS = 'aeiouAEIOU'

        if ' ' in word:
            word = ''.join(word.split())
        
        while indx < len(word) - 1: #dddaa
            if word[indx] not in VOWELS and word[indx + 1] not in VOWELS:
                count += 1
                indx += 1 
            elif count != 0:
                count_storage.append(count)
                count = 0
                indx += 1
            else:
                indx += 1
        count_storage.append(count)

        return max(count_storage)

    return (sorted(lst, key=count_adj_consonant, reverse=True))


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list) ==  ['dddaa', 'ccaa', 'aa', 'baa'])

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list) == ['salt pan', 'can can', 'batman', 'toucan'])

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list) == ['bar', 'car', 'far', 'jar'])

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list) == ['month', 'day', 'week', 'year'])

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list) == ['xxxx', 'xxxb', 'xxxa'])