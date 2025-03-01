# Write a function that takes a list of numbers and returns the sum of the 
# sums of each leading subsequence in that list. Examine the examples to see what we mean. 
# You may assume that the list always contains at least one number.


"""
P
I: List of numbers
O: sum of the sums of each leading subsequence in that list

E[0 + 0:1 + 0:2] etc
I

E
print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True

D
lists and slicing tools

A
this is a good use of slicing to get incremental slice of objects
have sum function of
create new list
slice : +1 to range of length of list length of list
put in new list and sum


only need 1 function. 

"""

def sum_of_sums(lst):
    new_lst = [lst[:indx + 1]
               for indx in range(len(lst))]
    
    final_lst = [num
                 for obj in new_lst
                 for num in obj]
   
    return sum(final_lst)



print(sum_of_sums([3, 5, 2]) == 21)               # True
#(3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True

#Their answer
def sum_of_sums(numbers):
    total_sum = 0
    running_sum = 0
    for num in numbers:
        running_sum += num
        total_sum += running_sum # performing this twice will add the subsequent number

    return total_sum

