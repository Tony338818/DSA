def number_of_islands(islandMap: list[list]):
    
    islands = 0
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    rows = len(islandMap)
    cols = len(islandMap[0])
    
    def dfs(r, c):
        
        if islandMap[r][c] == "0":
            return
        
        islandMap[r][c] = "0"
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if (
                0 <= nr < rows
                and 0 <= nc < cols
            ):
                dfs(nr, nc)
                
    for r in range(rows):
        for c in range(cols):
            if islandMap[r][c] == "1":
                islands += 1
                dfs(r, c)
                    
    return islands
        
    
islands_map = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


result = number_of_islands(islands_map)
print(result)