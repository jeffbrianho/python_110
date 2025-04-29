# In the previous exercise, you wrote a function that transposed a 3x3 matrix represented by a list of lists.

# Matrix transposes are not limited to 3x3 matrices, or even square matrices.
#  Any matrix can be transposed simply by switching columns with rows.

# Modify your transpose function from the previous exercise so that it works 
# with any MxN matrix with at least one row and one column.

"""

create columns or rows based on number of elements in inner list
lenouterlst = rows
for lsts in outer_lst
    lenlsts = column

append column to final maxtrix [[] [] [] [] [] []] X
for lst in outerlist
for object in rangelenlist
final list colum = append object
"""
def transpose(lst):
    final_lst = []
    for _ in range(len(lst[0])):
            final_lst.append([])

    for sub_lst in lst:
          for indx in range(len(sub_lst)):
                final_lst[indx].append(sub_lst[indx])
                
                       
    return final_lst 

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)

# Their answer
def transpose(matrix):
    transposed = []
    new_rows_count = len(matrix[0])

    for _ in range(new_rows_count):
        transposed.append([])

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            transposed[col_idx].append(matrix[row_idx][col_idx]) # they use the notation matrix [][] to grab element i used submatrix []

    return transposed