def spiral_matrix(matrix: list[list]):
    if not matrix: 
        return
    
    top = 0
    left = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix) - 1
    
    while top <= bottom and left <= right:
        
        for c in range(left, right + 1):
            print(matrix[top][c])
        top += 1
            
        for r in range(top, bottom + 1):
            print(matrix[r][right])
        right -= 1
            
        if top <= bottom:
            for c in range(right, left - 1, -1):
                print(matrix[bottom][c])
            bottom -= 1
            
        if left <= right:
            for r in range(bottom, top - 1, -1):
                print(matrix[r][left])
            left += 1
  
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
spiral_matrix(matrix)          