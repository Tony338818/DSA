"""
Given an integer array nums of unique elements, return all possible subsets (the power set). 
The solution set must not contain duplicate subsets, and you can return the solution in any order.
"""

def subsets(nums):
    
    subsets = []
    
    def backtrack(index, path):
        # Base case
        if index == len(nums):
            subsets.append(path[:])
            return
        
        # Choice : Take
        path.append(nums[index])
        
        # Recursive call
        backtrack(index + 1, path)
        
        # Undo -> Backtrack
        path.pop()
        
        # Choice : Skip
        backtrack(index + 1, path)
    
    backtrack(0, [])
    return subsets

nums = [1, 2, 3]
print(subsets(nums))
        
