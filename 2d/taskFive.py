from collections import deque

def flood_fill(image: list[list], sr: int, sc: int, color: int):
    if not image:
        return
    
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    rows = len(image)
    cols = len(image[0])
    
    old_color = image[sr][sc]
    queue = deque()
    queue.append((sr, sc))
    
    image[sr][sc] = color
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and image[nr][nc] == old_color
            ):
                image[nr][nc] = color
                queue.append((nr, nc))
                
                
    return image
    
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

sr = 1
sc = 1
color = 2

print(flood_fill(image, sr, sc, color))