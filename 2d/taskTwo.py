def rotate_matrix(matrix: list[list]):
    if not matrix:
        return 
    
    n = len(matrix)
    print(matrix)
    
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    print(matrix)    
    
    for row in matrix:
        row.reverse()
        
    print(matrix)    
    
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
rotate_matrix(matrix)
    