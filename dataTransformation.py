import numpy as np


# Rotates a matrix A such that
#
# |1 2|  _  |1 3|
# |3 4|  -  |2 4|
#
def rotate_matrix(mat):
    rot_mat = [["" for col in range(len(mat))] for row in range(len(mat[0]))]
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            rot_mat[col][row] = mat[row][col]
    return np.array(rot_mat)


# Used for converting letters to an adjusted ASCII value
def to_base26(letter, offset):
    return ord(letter) - offset


# Used to process letters from adj ASCII to Characters
def letters_from_base26(val, offset):
    out = ""
    last_ele = False
    while not last_ele:
        out = chr(val % 26 + offset) + out
        last_ele = val < 26
        val = int((val - (val % 26)) / 26)
        if not last_ele:
            val -= 1
    return out


#trims matrix so that all rows and columns are the same length
def matrix_trim(mat):
    col_diff = 0
    row_diff = 0
    max_col = 0
    max_row = 0
    for row in mat:
        if len(row) > max_col:
            max_col = len(row)
    for row in mat:
        if len(row) != max_col:
            col_diff = max_col - len(row)
    col_indices = []
    col_sizes = []
    for row in mat:
        for i in range(len(row)):
            col_indices.append(i)
    for i in range(len(mat[0])):
        col_sizes.append(col_indices.count(col_indices[i]))
    for i in range(len(mat[0])):
        if col_sizes[i] > max_row:
            max_row = col_sizes[i]
    for i in range(len(mat[0])):
        if col_sizes[i] != max_row:
            row_diff = max_row - col_sizes[i]
    if row_diff == 0 and col_diff == 0:
        return True
    return np.array([ele[:(max_row - row_diff + 1)] for ele in mat][:max_col - col_diff + 1])
