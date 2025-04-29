# Write a function that takes a list of words as input and returns a list of
# integers. Each integer represents the count of letters in the word that occupy
# their positions in the alphabet.


"""
create a key to follow with letter to index


"""
COMPARE_LIST = list('abcdefghijklmnopqrstuvwxyz') 

def solve(lst_of_words):
    final_lst = []
    for word in lst_of_words:
        counter = 0
        for index, char in enumerate(word):
            if char.lower() == COMPARE_LIST[index]:
                counter += 1
        final_lst.append(counter)
    return final_lst

print(solve(["abode","ABc","xyzD"]) == [4, 3, 1])
print(solve(["abide","ABc","xyz"]) ==  [4, 3, 0])