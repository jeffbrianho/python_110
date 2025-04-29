
"""
1   2   3

4   5   6

7   8   9    [2][0] >> [0][0] [1][0] >> [0][1] [0][0] >> [0][2]
            [2][1] >> [1][0] [1][1] >> [1][1] [0][1] >>[1][2]
-----------
7   4   1

8   5   2

9   6   3

if the row is x long the new rotation should be x wide
if the column is y wide their should be y long

len(matrix[0]) = new_width (how many element in  sublist)
for sub_matrix in matrix
    len(submatrix) = new_length (how many sublists)
"""



def rotate90(matrix):
    new_lst = []
    for _ in range(len(matrix[0])):
        new_lst.append([])

    for row_amount in range(len(matrix[0])): # 0, 1, 2, 3
        for column_amount in range((len(matrix) - 1), -1, -1): # 1, 0
            new_lst[row_amount].append(matrix[column_amount][row_amount])
    
    return new_lst


matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8], 
]# [1][0] >[0][0], [0][0] > [0][1]
# [1][1] >[1][0], [0][1] > [1][1]
# [1][2] > [2][0] ,[0][2] > [2][1]
# [1][3] > [3][0] , [0][3] > [3][1]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)

# their answer
def rotate90(matrix):
    rotated = []
    new_rows_count = len(matrix[0])

    for _ in range(new_rows_count):
        rotated.append([])

    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):
            rotated[col_idx].append(matrix[row_idx][col_idx])

    for row in rotated:
        row.reverse()

    return rotated