# A 3x3 matrix can be represented by a list of nested lists: 
# an outer list that contains three sub-lists that each contain three elements. 
# For example, the 3x3 matrix shown below:

# 1  5  8
# 4  7  2
# 3  9  6

# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]

# The transpose of a 3x3 matrix is the matrix that results from exchanging the rows 
# and columns of the original matrix. For example, the transposition of the matrix shown above is:

# 1  4  3
# 5  7  9
# 8  2  6

# Write a function that takes a list of lists that represents a 3x3 matrix and returns 
# the transpose of the matrix. You should implement the function on your own, without using 
# any external libraries.

# Take care not to modify the original matrix -- your function must produce a new matrix and 
# leave the input matrix list unchanged.

"""
I: NESTED LIST
O: transposed listed (new not mutated)
E: 0 indx in 1 list 1 index in next 2 index in next
I

E
D: lsts
A:
go through each list and append the first index "0" to a list and append to final list
do the same with 1 and 2 .
return list


"""

def transpose(matrix):
    holding_lst1 = [lst[0] for lst in matrix]
    holding_lst2 = [lst[1] for lst in matrix]
    holding_lst3 = [lst[2] for lst in matrix]
    
    return [holding_lst1, holding_lst2, holding_lst3]


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

# Their answer
def transpose(matrix):
    transposed = []
    new_rows_count = len(matrix[0])

    for _ in range(new_rows_count): # transposed = [[],[],[]]
        transposed.append([])

    for row_idx in range(len(matrix)): # row_idx = 0, 1, 2
        for col_idx in range(len(matrix[row_idx])): # col_idx = range(3) 0, 1, 2
            transposed[col_idx].append(matrix[row_idx][col_idx]) # transposed[0].append(matrix[0][0>1>2])adds to new sub list each time. [[1], [5], [8]]

    return transposed