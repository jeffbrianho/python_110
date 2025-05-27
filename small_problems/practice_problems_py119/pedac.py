
# BOUNCY COUNT
# Some numbers have only ascending digits, like 123, 3445, 2489, etc.
# Some numbers have only descending digits, like 321, 5443, 9842, etc.
# A number is "bouncy" if it has both ascending and descending digits, like 313, 92543, etc.
# Write a method that takes a list of numbers and counts how many of them are bouncy.

"""

P
Some numbers will be ascending, some descending, we are looking for numbers that go up and down - then are bouncy. Return the frequency of bouncy numbers.

Rules/Requirements
- numbers > 0
- to be bouncy, a number must have at least three digits
- can have a lot of digits, but would only need to find three that were bouncy
- return zero if the input is []

Data
Input: array/list of integers
Output: integer/count
Intermediate:
  - string of input number so that you can iterate through the digits
  - array/list of digits as integers/strings
  - list/array of booleans corresponding to whether a number in the input array/list is bouncy
  - list/array of bouncy numbers

A:
high level strategy:
focus on the hard part of the problem

/*
BOUNCY COUNT
Some numbers have only ascending digits, like 123, 3445, 2489, etc.
Some numbers have only descending digits, like 321, 5443, 9842, etc.
A number is "bouncy" if it has both ascending and descending digits, like 313, 92543, etc.
Write a method that takes a list of numbers and counts how many of them are bouncy.

P
Some numbers will be ascending, some descending, we are looking for numbers that go up and down - then are bouncy. Return the frequency of bouncy numbers.

Rules/Requirements
- numbers > 0
- to be bouncy, a number must have at least three digits
- can have a lot of digits, but would only need to find three that were bouncy
- return zero if the input is []

Data
Input: array/list of integers
Output: integer/count
Intermediate:
  - string of input number so that you can iterate through the digits
  - array/list of digits as integers/strings
  - list/array of booleans corresponding to whether a number in the input array/list is bouncy
  - list/array of bouncy numbers

High-level strategies
Jeff 
  - empty list, return 0. 
  - Fewer digits that 3, not bouncy.
  - iterate through each digit, record if goes up, or down. If they go up and down, they are bouncy
  - returning how many are bouncy

  - or record if goes up or down, then looking for the opposite

Will
  - iterate over an array of integers, compare currentIndex with nextIndex, set flags for going up or down, if both are true at the end it is bouncy

Joel
  - iterate over a string of the input number, for each digit check if less than the next digit, add true/false to a new list, at the end of the number, if true and false are both in there, it is bouncy. Ignore if equal to.

Clare
  - Check if the number is ascending, if so, return false. Reverse it, check if ascending, if so, return false. Otherwise return true.

  
Algorithm:


Check if list is empty
    - return 0 

create helper function `is_bouncy`
    - convert int to string:
        if len(string) < 2:return False
    - iterate through each char from its index using range(len + 1) (check for off 1 error)
        store boolean in list [if strnum[indx] <= strnum[indx + 1] add boolean until iterated through]
        if all True - not bouncy (return False)
    - check if greater string
        store boolean in list [if strnum[indx] >= strnum[indx + 1] add boolean until iterated through]
        if all True - not bouncy (return False)
    - else it is bouncy return string

- iterate through each object and create a final list
    - if is_bouncy(num), add to list; else do nothing
    - return length of new list

"""

def bouncyCount(lst):
    if not lst:
        return 0
    
    def is_bouncy(num):
        s_num = str(num)
    
        
        if len(s_num) <= 2:
            return False
        
        if all(([s_num[indx] <= s_num[indx +1] for indx in range(len(s_num) - 1)])) or \
            all([s_num[indx] >= s_num[indx +1] for indx in range(len(s_num) - 1)]):
            return False
        else:
            return True
    
    return len([num for num in lst
                if is_bouncy(num)])


# Python test cases:
print(bouncyCount([]) == 0)
print(bouncyCount([11, 0, 345, 21]) == 0)
print(bouncyCount([121, 4114]) == 2)
print(bouncyCount([176, 442, 80701644]) == 2)
