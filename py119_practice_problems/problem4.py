# Create a function that takes a list of integers as an argument and returns a tuple of two numbers 
# that are closest together in value. If there are multiple pairs that are equally close, return the 
# pair that occurs first in the list.

"""
p
i: list
o: tuple
e: return a tuple of the numbers with the smallest difference?
i


e: 11 and 15 diff 4; 25, 27 differnce of 2 must keep same order due to first. 
d: list of differences? key difference; value tuple? dicts will keep order
a:
iterate through each list inx 
use nested loop to iterate through each number + 1 until end
check this first
create a dictionary of difference of numbs: tuple of nums
return the lowest dict value


"""

def closest_numbers(lst):
    dict_of_tuples ={(reference_num, checking_num): abs(reference_num - checking_num)
            for indx, reference_num in enumerate(lst)
            for checking_num in lst[indx + 1:]}
    
    def key_swap(dictionary):
        return [dictionary[1]]
            
    return sorted(dict_of_tuples.items(), key=key_swap)[0][0]
            


print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# 25 mins
# ** practice getting the values from the key value. create a tuple with items() 
# and use key swap to  get the second value (key, value)