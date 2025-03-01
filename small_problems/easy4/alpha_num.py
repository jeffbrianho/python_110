# Write a function that takes a list of integers between 0 and 19 and returns 
# a list of those integers sorted based on the English word for each number:

# zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve,
#  thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen




"""
I list of integers between 0 - 19
O list of integers sorted based on word for each number
E sort by the alpha name
I

E 

D

A
associate the index with the string name if 1, associate alphalist to lst[1] = 'one'
use sorted function with key=alphalist function

"""
STRING_CONTSTANT = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

# STRING_DICTIONARY= {}
# for index, word in enumerate(STRING_CONTSTANT):
#     STRING_DICTIONARY[word] = index


# def string_list(lst):
#     string_lst = []

#     for num in lst:
#         string_lst.append(STRING_CONTSTANT[num])
    
#     return string_lst

# def alphabetic_number_sort(lst):
#     final_list = []
#     sorted_string_lst = (sorted(string_list(lst)))
#     for spelled_num in sorted_string_lst:
#         final_list.append(STRING_DICTIONARY[spelled_num])
    
#     return (final_list)


   
def word_for_num(num):
    return STRING_CONTSTANT[num]

        
def alphabetic_number_sort(lst):
    return sorted(lst, key=word_for_num)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]




print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

#*** skill set, string number to indexed list. use as a key for sorting, access with index access
# when a key is used it makes an almost key value pair or a tuple sorts the key then returns the original value. the return 
# is first ie ... ("zero", 0),("one", 1) - word_for_num inputs num = 0 and returns "zero"; sorted then sorts the first object at 
# each index 0 then returns the original object at index 1