# Create a function that takes a string argument and returns a copy of the string with every 
# second character in every third word converted to uppercase. Other characters should remain the same.


"""
P
I: string
O: copy of string second char in 3rd word converted to upper leave same
E
I

E: 
D:
 lists containing each word
 strings
A:

create a list of words
    - use split()
iterate through each word and change every 3rd word, 2, 5, 8, (range 0, len, 3)
    - for loop with range
    - use helper function to change every other if single letter return letter
save to new list, 
join list
    - ' '. join()
return string

"""

def to_weird_case(string):

    def change_word(word):
        final_word = ''

        if len(word) == 1:
            return word
        
        for indx, char in enumerate(word):
            if indx % 2 != 0:
                final_word += char.upper()
            else:
                final_word += char.lower()

        return final_word


    string_lst = string.split()

    final_lst = [change_word(string_lst[indx]) 
                 if indx in range(2, len(string_lst), 3)
                 else string_lst[indx]
                 for indx in range(len(string_lst))]
    
    return ' '.join(final_lst)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)


# 13:13 mins