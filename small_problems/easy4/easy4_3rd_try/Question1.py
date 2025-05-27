# Write a function that takes a list of integers between 0 and 19 and returns a 
# list of those integers sorted based on the English word for each number:

# zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, 
# fourteen, fifteen, sixteen, seventeen, eighteen, nineteen


"""
list of ints
list of ints: doeesnt specify copy or mutation

sorted by english word for each number

make a key to link word to number, 
another list based off of index. 

make key index access [0] returns string zero
sorted function
return list

"""

def alphabetic_number_sort(lst):

    ALPHA_SORT = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 
                  'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                    'nineteen']
    
    def sort_key(num):
        return ALPHA_SORT[num]
    
    return sorted(lst, key=sort_key)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

# 4:27 use of key_sort
