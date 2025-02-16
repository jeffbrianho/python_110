# Write a function that takes a list of numbers and returns a list with the same number of elements, 
# but with each element's value being the running total from the original list.

"""
P:
INPUT: list of numbers
OUTPUT: list with same number of elements with each element being a total from the original list
EXPLICIT: the next number should be the addition: and progressed. 
IMPLICIT: only number are given empty lists return empty

E:
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

D: lists

A:
create empty list:
add spot 1 to list: add previous number to next number and add to list until all number are met
return new list

C

"""
def running_total(num_list):
    final_list = []

    for num in num_list:
        if final_list == []:
            final_list.append(num)
        else:
            final_list.append(num + final_list[-1])
            
    return final_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True