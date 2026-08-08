"""
Problem:
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0.

Solution
1. Create a list to store the coordinates of the zeros.
2. Use a nested loop to find all the zeroes in the matrix and append them to the coordinates list.
4. Use a new loop through the coordinates, get each rows and columns and, use a loop to update the values there to zero.
"""

def set_to_zero(matrix: list[list]):
    if not matrix:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    rows_to_zero = set()
    cols_to_zero = set()
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
               rows_to_zero.add(r)
               cols_to_zero.add(c)
                
    for r in range(rows):
       if r in rows_to_zero:
           for c in range(cols):
               matrix[r][c] = 0  
               
    for c in range(cols):
       if c in cols_to_zero:
           for r in range(rows):
               matrix[r][c] = 0  
                
    print(matrix)
    
    
def set_to_zero_optimized(matrix: list[list]):
    if not matrix:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    first_row_zero = False
    first_col_zero = False

    for c in range(cols):
        if matrix[0][c] == 0:
            first_row_zero = True
            break

    for r in range(rows):
        if matrix[r][0] == 0:
            first_col_zero = True
            break
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0
                
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    
    # for row in range(rows):
    #     if matrix[row][0] == 0:
    #         for c in range(cols):
    #             matrix[row][c] = 0
                
    # for col in range(cols):
    #     if matrix[0][col] == 0:
    #         for r in range(rows):
    #             matrix[r][col] = 0
                
    print(matrix)
                
                
                
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
set_to_zero_optimized(matrix)