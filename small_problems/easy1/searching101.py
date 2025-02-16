# Write a program that solicits six (6) numbers from the user and prints a message that 
# describes whether the sixth number appears among the first five.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.

"""
P:
Input: 6 Integers
Output: String assessing containment of 6th integer in last 5
Explicit: explain if the 6th integer is in the last 5
Implicit

E: only integers are given
D: use a collection like a list to assess

A: collect all numbers
compare if last number is in collection
return if yes or no

Input strings: for 6 numbers
create empty list to supply 5 numbers
if 6th number in list provide string saying it is
or string saying it is not

"""

numbers = []

num1 = input('Enter the 1st number: ')
numbers.append(num1)
num2 = input('Enter the 2nd number: ')
numbers.append(num2)
num3 = input('Enter the 3rd number: ')
numbers.append(num3)
num4 = input('Enter the 4th number: ')
numbers.append(num4)
num5 = input('Enter the 5th number: ')
numbers.append(num5)
num6 = input('Enter the last number: ')

if num6 in numbers:
    print(f'{num6} is in {num1},{num2},{num3},{num4},{num5}.')
else:
    print(f"{num6} isn't in {num1},{num2},{num3},{num4},{num5}.")

# 17 is in 25,15,20,17,23.

# 18 isn't in 25,15,20,17,23.