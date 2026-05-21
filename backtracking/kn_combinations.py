"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range 1 to n. 
You may return the answer in any order.
"""
def combination(k, n):
    combinations = []
    
    def backtrack(start, path):
        # Base case
        if len(path) == k:
            combinations.append(path[:])
            return
        
        for num in range(start, n + 1):
            if num in path:
                continue
            
            # Choice: Take
            path.append(num)
            
            # Recursive call
            backtrack(num + 1, path)
            
            # Undo -> Backtrack
            path.pop()
            
    backtrack(1, [])
    return combinations
        

n, k = 4, 2
print(combination(k, n))
