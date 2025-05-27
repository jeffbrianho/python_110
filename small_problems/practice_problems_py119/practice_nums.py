# Basic​: Create a function called matrix_element_sum that takes a 2D list (matrix) as
#  an argument and returns the sum of all elements.



# def matrix_element_sum(matrix):
#     return sum([sum(matrix[0]), sum(matrix[1])])

# # Examples
# print(matrix_element_sum([[1, 2], [3, 4]]) == 10)
# print(matrix_element_sum([[1, 2, 3], [4, 5, 6]]) == 21)
# print(matrix_element_sum([[0, 0], [0, 0]]) == 0)
    
# Intermediate​: Create a function called subarray_sum that takes a list of integers and an integer k. 
# Return a list of all subarrays of length k and their sum.

"""
I: list of int, k(int)
O: tuple ( sub arrays length k and their sum?)
only acsending range

for index, index + k sub array
return [num, num], sum[num num]

"""

# def subarray_sum(nums, k):
#     return [(nums[indx:indx + k], sum(nums[indx:indx + k])) for indx in range(len(nums))
#             if len(nums[indx:indx + k]) == k]
  
# # Examples
# print(subarray_sum([1, 2, 3, 4], 2) == [([1, 2], 3), ([2, 3], 5), ([3, 4], 7)])
# print(subarray_sum([1, 2, 3], 3) == [([1, 2, 3], 6)])
# print(subarray_sum([5, 5, 5], 2) == [([5, 5], 10), ([5, 5], 10)])



# Intermediate​: Create a function called diagonal_sum that takes a square matrix 
# (2D list with equal rows and columns) and returns the sum of both diagonals.
#  Each element that appears in both diagonals should be counted only once.

"""
p
i: square matrix 4/4
o: sum of both diagnolas
e
i: if length < 2 then sum everything
if length > 2


e
d
a:

for range length [elements] 
    if not in storage:
    append lstindx[indx] and index[-indx]

"""

# def diagonal_sum(matrix):
#     storage_list = []

#     for index in range(len(matrix)):
#         if matrix[index][index] != matrix[index][(len(matrix) - 1) - index]:
#             storage_list.append([matrix[index][index], matrix[index][(len(matrix) - 1) - index]])
#         else: 
#             storage_list.append([matrix[index][index]])

#     def unpack(nested_lst):
#         return [obj for lst in (nested_lst)
#                     for obj in lst]
    
#     return sum(unpack(storage_list))

# # Examples
# print(diagonal_sum([[1, 2], [3, 4]]) == 10)  # 1 + 2 + 3 + 4
# print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 25)  # 1 + 3 + 5 + 7 + 9
# print(diagonal_sum([[7]]) == 7)

#  ​Advanced​: Create a function called count_word_in_grid that takes a 2D grid of characters and a word.
#  Return the number of times the word appears in the grid horizontally, vertically, or diagonally.

"""
I: 2D grid of char, word
O: return the number of time it appears hor ver diag

all the substrings from each row, each list and each diagonal
put them in a list, and use list.count(word) and return the number

# for sublist in lst "join" and append # get rows
# vert list holder
#   - for zip(lst) append "join" # get verticals
# # diagonal holder
# #   - for indx[indx] [indx][len(lst) - 1 - indx] if not the same # gets diagnols

# append all to single list of words. and count
# """

# def count_word_in_grid(grid, word):
#     sub_list_holder = []

#     for sub_list in grid:                               # gets horizontal
#             sub_list_holder.append(''.join(sub_list))
    
    
#     for indx in range(len(grid)):                       # gets vertical
#         vert_word = ''
#         for sub_indx in range(len(grid)):
#             vert_word += grid[sub_indx][indx]
#         sub_list_holder.append(vert_word)

#     diag_word = ''
#     for diag_indx in range(len(grid)):
#         diag_word += grid[diag_indx][diag_indx]

#     sub_list_holder.append(diag_word)

#     rdiag_word = ''
#     for rdiag_indx in range(len(grid)):
#         rdiag_word += grid[rdiag_indx][len(grid) - 1 - rdiag_indx]
    
#     sub_list_holder.append(rdiag_word)

#     return sub_list_holder.count(word)
# # Examples
# grid1 = [
#     ['a', 'b', 'c'],
#     ['d', 'o', 'g'],
#     ['e', 'f', 'g']
# ]
# print(count_word_in_grid(grid1, "dog") == 1)

# grid2 = [
#     ['c', 'a', 't'],
#     ['a', 'a', 'a'],
#     ['t', 'a', 'c']
# ]
# print(count_word_in_grid(grid2, "cat") == 2)




# Write a function that computes the difference between the square of the sum of the 
# first count positive integers and the sum of the squares of the first count positive integers.

# def sum_square_difference(num):
#     def sum_squared(value):
#         return sum([value for value in range(1, value + 1)])**2
     
#     def sum_of_squares(value):
#          return sum([value**2 for value in range(1, value + 1)])
     
#     return (sum_squared(num) - sum_of_squares(num))

# print(sum_square_difference(3) == 22)          # True
# # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

# print(sum_square_difference(10) == 2640)       # True
# print(sum_square_difference(1) == 0)           # True
# print(sum_square_difference(100) == 25164150)  # True

# Write a function that takes a string and returns a dictionary containing the following three properties:

# the percentage of characters in the string that are lowercase letters
# the percentage of characters that are uppercase letters
# the percentage of characters that are neither
# All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

# You may assume that the string will always contain at least one character.

"""
I:STRING
O: DICT WITH PERCENTAGES
E
I

E

D

A

# """

# def letter_percentages(string):
    
#     total = len(string)
#     lowercase = 0
#     uppercase = 0
#     neither = 0

#     for char in string:
#         if char.isupper():
#             uppercase += 1
#         elif char.islower():
#             lowercase += 1
#         else:
#             neither += 1

#     final_dict = {
#     'lowercase': f'{(lowercase / total * 100):.02f}',
#     'uppercase': f'{(uppercase / total * 100):.02f}',
#     'neither': f'{(neither/ total * 100):.02f}',}

#     return final_dict

# expected_result = {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# }
# print(letter_percentages('abCdef 123') == expected_result)

# expected_result = {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# }
# print(letter_percentages('AbCd +Ef') == expected_result)

# expected_result = {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# }
# print(letter_percentages('123') == expected_result)

# A featured number (something unique to this exercise) is an odd number that 
# is a multiple of 7, with all of its digits occurring exactly once each. 
# For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7),
#  and 133 is not (the digit 3 appears twice).

# Write a function that takes an integer as an argument and returns the next featured number 
# greater than the integer. Issue an error message if there is no next featured number.

# NOTE: The largest possible featured number is 9876543201

"""
create an is featured num function
    is odd
    is mulitple of 7
    no repeats
    RETURN if `all` true

num += 1 to skip
while num is not a featured num
    num += 1

return num 

    
"""

def next_featured(num):

    def is_featured(num):
        def is_odd(num):
            return num % 2 == 1
        
        def is_mult_7(num):
            return num % 7 == 0
        
        def is_unique(num):
            string_num = str(num)
            return all([string_num.count(num) == 1 for num in string_num])
        
        return all([is_odd(num), is_mult_7(num), is_unique(num)])
    
    num += 1
    if num >= 9876543201:
        return "There is no possible number that fulfills those requirements."
    else:
        while not is_featured(num):
            num += 1
        
        return num 


# print(next_featured(12) == 21)                  # True
# print(next_featured(20) == 21)                  # True
# print(next_featured(21) == 35)                  # True
# print(next_featured(997) == 1029)               # True
# print(next_featured(1029) == 1043)              # True
# print(next_featured(999999) == 1023547)         # True
# print(next_featured(999999987) == 1023456987)   # True
# print(next_featured(9876543186) == 9876543201)  # True
# print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True