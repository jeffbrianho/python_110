# Create a function that takes a list of integers as an argument and returns a 
# tuple of two numbers that are closest together in value. If there are multiple 
# pairs that are equally close, return the pair that occurs first in the list.

"""

P
I: list of integers
O: tuple of integers of numbers that are closest together 

E return pair that occurs first in list

I

E
D: dictionary of tuple and sum
return the lowest value?

A:
create a dictionary of each tuple to maintain order
    - iterate through each element
        for first element in lst
            for lst[indx] in range(indx + 1, len(lst))
    - use tuple: difference of tuple in list of tuples

get the abs difference of each tuple and create that value


return the key of the lowest value using [0]
    - key value
    return value of dictioanry
can sort by min value and return first min key?
    min dictionary 
    return key

C

"""

def closest_numbers(lst):
    list_tups = ([(ele, lst[next_ele]) for indx, ele in enumerate(lst)
        for next_ele in range(indx + 1, len(lst))])

    dict_of_tups_and_diff = {tup: abs(tup[0] - tup[1]) for tup in list_tups}

    def min_value_key(key):
        return dict_of_tups_and_diff[key]

    return (sorted(dict_of_tups_and_diff, key=min_value_key)[0])


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# 17:34 mins good use of keys, practice key dicts ***
