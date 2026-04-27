"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Solution:
1. count all the fresh oranges in the grid
2. create a queue and initialize it to all the positions in our grid that contains a rotten orange
3. initialize the bfs
"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        freshOranges = 0
        queue = []
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))                
                    
        
        while queue and freshOranges > 0:
            size = len(queue)
            infected = False
            
            for i in range(size):
                r, c = queue.pop(0)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            freshOranges -= 1
                            queue.append((nr, nc))
                            infected = True
                            
            if infected:
                minutes += 1
                
        return minutes if freshOranges == 0 else -1
                            
                    
        
                    

sol = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
result = sol.orangesRotting(grid=grid)
print(result)

        