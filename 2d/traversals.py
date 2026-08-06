
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



matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# row_wise_traversal(matrix)
zigzag_traversal(matrix)