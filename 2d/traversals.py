
def row_wise_traversal(matrix: list[list]):
    row = len(matrix)
    col = len(matrix[0])
    
    for r in range(row):
        for c in range(col):
            print(matrix[r][c])
            
        print(f'row {r} done')
        

def col_wise_traversal(matrix: list[list]):
    row = len(matrix)
    col = len(matrix[0])
    
    for c in range(col):
        for r in range(row):
            print(matrix[r][c])
            
        print(f'col {c} done')


def reverse_row_traversal(matrix: list[list]):
    row = len(matrix)
    col = len(matrix[0])
    
    for r in range(row):
        for c in range(col - 1, -1, -1):
            print(matrix[r][c])
            
        print(f'row {r} done')
        

def bottom_up_traversal(matrix: list[list]):
    row = len(matrix)
    col = len(matrix[0])
    
    for r in range(row - 1, -1, -1):
        for c in range(col):
            print(matrix[r][c])
            
        print(f'row {r} done')
        

def zigzag_traversal(matrix: list[list]):
    row = len(matrix)
    col = len(matrix[0])
    
    for r in range(row):
        if r % 2 == 0:
            for c in range(col):
                print(matrix[r][c])  
        else:
            for c in range(col -1, -1, -1):
                print(matrix[r][c])
                

def boundary_traversal(matrix: list[list]):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows == 1:
        for c in cols:
            print(matrix[0][c])
            
    if cols == 1:
        for r in rows:
            print(matrix[r][0])
    
    for c in range(cols):
        print(matrix[0][c])
        
    for r in range(1, rows):
        print(matrix[r][cols - 1])
        
    for c in range(cols - 2, -1, -1):
        print(matrix[rows - 1][c])
        
    for r in range(rows - 2, 0, -1):
        print(matrix[r][0])
        
        
def main_diagonal_traversal(matrix: list[list]):
    if not matrix:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Why min(rows, cols)?
    # Because rectangular matrices may not have the same number of rows and columns.
    
    for i in range(min(rows, cols)):
        print(matrix[i][i])
        
def secondary_diagonal_traversal(matrix: list[list]):
    if not matrix :
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    for r in range(min(rows, cols)):
        c = cols - 1 - r
        print(matrix[r][c])
            
            
def both_diagonals(matrix: list[list]):
    if not matrix:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    for r in range(rows):
        print(matrix[r][r])
        
        secondary = cols - 1 - r
        if secondary != r:
            print(matrix[r][secondary])
            

def anti_diagonal_traversal(matrix: list[list[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    for diagonal_sum in range(rows + cols - 1):
        for r in range(rows):
            c = diagonal_sum - r

            if 0 <= c < cols:
                print(matrix[r][c])

matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8], 
          [9, 10, 11, 12]]
# row_wise_traversal(matrix)
both_diagonals(matrix)