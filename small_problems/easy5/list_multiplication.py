# Given two lists of integers of the same length, 
# return a new list where each element is the product of the 
# corresponding elements from the two lists.

"""
P
I: list of 2 ints same length
O: new list each element is product of the elements of two lists

E: the index of 1 list mulitiplied by same indexed element of other list 

I: only numbers

E:
list_a = [1, 2, 3]
list_b = [4, 5, 6]

D:lists

A:
create final_list
can use a counter index like enumerate 
append the lsta[ind] * lstb [ind] to final list
return final list


"""

def multiply_items(lst1, lst2):
    # return [num * lst2[indx] for indx, num in enumerate(lst1)]

    return [tup[0] * tup[1] for tup in list(zip(lst1, lst2))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

#Their answer
def multiply_items(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])

    return result

# range is cleaner than enumerate as the numbers will be the same index