# DONE 3:13 mins

# Write a function that takes a list of integers between 0 and 19 and returns a list of 
# those integers sorted based on the English word for each number:

# zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve,
#  thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

ALPHA_LIST = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 
              'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
              'sixteen', 'seventeen', 'eighteen', 'nineteen']

def alphabetic_number_sort(lst):

    def key_alpha(num):
        return ALPHA_LIST[num]
    
    return sorted(lst, key=key_alpha)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True