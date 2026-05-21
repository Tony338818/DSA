"""
Given an array nums of distinct integers, return all the possible permutations (all the different ways you can arrange the numbers).
You can return the answer in any order.
"""

def permutations(nums):
    
    permutations = []
    
    def backtrack(path):
        # base case
        if len(path) == len(nums):
            permutations.append(path[:])
            return
        
        # Choice: Take
        for num in nums:
            if num in path:
                continue
            path.append(num)
        
            # Recursive call
            backtrack(path)
        
            # Undo -> Backtracking
            path.pop()
            
    backtrack([])
    return permutations

print(permutations([1, 2, 3]))