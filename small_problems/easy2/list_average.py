# 1 min DONE
def average(lst):
    return sum(lst)//len(lst)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True


# Write a function that takes one argument, a list of integers, and returns the average of 
# all the integers in the list, rounded down to the integer component of the average. 
# The list will never be empty, and the numbers will always be positive integers.

"""
P
I: list of integers
O: average of all the integers in the list
E: rounded down to the integer cmoponenet of the average. positive integers and no empty lists
I

E
D
Alist comprehension. multiplying last one div by len of list?




"""

def average(lst):
#    return (sum(lst)//len(lst))


    sum = 0
    for num in lst:
        sum += num
    return (sum//len(lst))


print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True

def average(lst):
    sum_of_lst = sum(lst)
    return sum_of_lst // len(lst)

# 1 min