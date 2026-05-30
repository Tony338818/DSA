"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        result = []
        
        while left <= right and top <= bottom:
            # move left
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # move down
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            if top <= bottom:
                # move left
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
                
            if left <= right:
                # move up
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
                
        return result
    
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = sol.spiralOrder(matrix)
print(result)