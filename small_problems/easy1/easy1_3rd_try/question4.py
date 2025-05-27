# Write a function that takes a list of numbers and returns a list with the same number of elements, 
# but with each element's value being the running total from the original list.

def running_total(lst):
    # total = 0
    # new_list = []
    # for num in lst:
    #     total += num
    #     new_list.append(total)
    
    # return new_list

    return [sum(lst[:indx]) for indx in range(1, len(lst) + 1)]

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

# 2:03 mins some use a slicing method to arrive at similar solution 
# took some time to get to sum function maybe consider pedac?
