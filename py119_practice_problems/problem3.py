# Create a function that takes a string argument and returns a copy of the string with 
# every second character in every third word converted to uppercase. Other characters should remain the same.

"""
I: String
O: string
E: return copy of string with second char in third word upper everything else the same

E: 0, 1, 2(iS), 3, 4, 5(tExT), 6, 7, 8(pRiNtInG)

D: list

A:
take each word and transform each 3rd word to alt chars

make the sentence into a list of words
range through every 3rd perform an action - counter ? while?
3rd word changed to every upper - functionhelper?
save to new string, 
return string 
"""

def to_weird_case(sentence):

    def modify_word(word):
        new_word = '' 
        for indx, char in enumerate(word):
            if indx % 2 == 0:
                new_word += char.lower()
            else:   
                new_word += char.upper()
        return new_word
    
    list_of_words = sentence.split()
    
    counter = 1
    final_string_list = []
    for word in list_of_words:
        
        if counter != 3:
            final_string_list.append(word)
            counter += 1
        else:
            final_string_list.append(modify_word(word))
            counter = 1
    
    return ' '.join(final_string_list)

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