# Create a function that takes a list of numbers as an argument.
#  For each number, determine how many numbers in the list are smaller than it,
#  and place the answer in a list. Return the resulting list.

# When counting numbers, only count unique values. That is, if a number occurs multiple
# times in the list, it should only be counted once.

"""
P
I: list 
O: list
E: find how many numbers are smaller than current number and return that amount
I

E
D
A
start number: and iterate through
iterate again through the list starting with indx + 1 and have counter for each num < current num
return to list


"""

def smaller_numbers_than_current(lst):
    final_lst = []

    for current_num in lst: 
        count = 0
        for compare_num in set(lst):
            # print(compare_num,current_num)
            
            if current_num > compare_num:
                count += 1
        final_lst.append(count)
    return final_lst

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

# time 10 mins: 
# theme: compare numbers to current set 
# use set to reduce dups, iterate through each using nested loop
