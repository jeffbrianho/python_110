# Create a function that takes a list of numbers as an argument.
#  For each number, determine how many numbers in the list are smaller than it,
#  and place the answer in a list. Return the resulting list.

# When counting numbers, only count unique values. That is, if a number
#  occurs multiple times in the list, it should only be counted once.

"""
P
I list of numbers
O: list of numbers smaller than it
E: only count numbers once create a list of all the numbers that have numbers smaller than it
I

E: 

D: set() to compare numbers separately - dont need to worry about same just lower
list

A: 
create a unique set list to iterate through. 
create a count if number is < current number in list +1 count and return final count
iterate through each number in given list and compare to set. 


"""

def smaller_numbers_than_current(lst):
    set_reference = set(lst)
    
    new_lst = []

    for num in lst:
        count = 0
        for comparison in set_reference:
            if num > comparison:
                count += 1
        new_lst.append(count)
    
    return new_lst

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

# 6:46 mins - nested iteration 