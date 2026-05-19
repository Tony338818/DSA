"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        rows = {}
        cols = {}
        boxes = {}
        
        for r in range(9):
            for c in range(9):
                
              value = board[r][c]  
              
              if value == '.':
                  continue
              
              box = (r // 3, c // 3)
              
              if r not in rows:
                  rows[r] = set()
                  
              if c not in cols:
                  cols[c] = set()
                  
              if box not in boxes:
                  boxes[box] = set()
                  
              if (
                  value in rows[r] or
                  value in cols[c] or
                  value in boxes[box]
              ): return False
              
              
              rows[r].add(value)
              cols[c].add(value)
              boxes[box].add(value)
              
        return True

                