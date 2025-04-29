# You've just discovered a square (NxN) field and you notice a warning sign.
# The sign states that there's a single bomb in the 2D grid-like field in front
# of you.

# Write a function `mine_location` that accepts a 2D array, and returns the
# location of the mine. The mine is represented as the integer 1 in the 2D array.
# Areas in the 2D array that are not the mine will be represented as 0s.

# The location returned should be an array where the first element is the row index, 
# and the second element is the column index of the bomb location (both should be 0 based).
#  All 2D arrays passed into your function will be square (NxN), and there will only be one mine in the array.

"""
P
I 2-d array (nested list)
O: location [index. column]
E: only 1 mine
I

E
D
A:
can use enumerate to obtain index and place in final 
outer list iterate inner list iterate
return the num if not 0 or == 1


"""
def mine_location(outer_list):
    nested_list = [[outer_index, inner_index]  for outer_index, inner_list in enumerate(outer_list)
                                        for inner_index, value in enumerate(inner_list)
                                        if value == 1]
    
    return [value   for list in nested_list
                    for value in list]


# Examples:
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == [0, 0])
print(mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [1, 1])
print(mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) == [2, 1])
print(mine_location([[1, 0], [0, 0]]) == [0, 0])
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == [0, 0])
print(mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == [2, 2])