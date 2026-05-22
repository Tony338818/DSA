"""
Given an (m x n) grid of characters called board and a string word, return True if word exists in the grid. 

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. The same letter cell may not be used more than once in a single word path
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        rows = len(board)
        cols = len(board[0])
        directions = [(0,1), (0,-1), (1, 0), (-1,0)]
        visited = set()
        
        def backtrack(r, c, word_idx):
            # constraints
            if(r < 0 or r >= rows or
               c < 0 or c >= cols or
               board[r][c] != word[word_idx]
               ): return False
            
            # Base Case
            if word_idx == len(word) - 1:
                return True
            
            # Choice: Take
            visited.add((r, c))
            
            # Check Neighbors
            # Recursive Call
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, word_idx + 1):
                    return True                 
                  
            # Undo -> Backtrack
            visited.remove((r, c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
                
        return False

sol = Solution()    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(sol.exist(board, word))

