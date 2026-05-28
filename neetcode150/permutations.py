"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(path):
            # base case
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            # take   
            for num in nums:
                if num in path:
                    continue
                path.append(num)
            
                # recursive call
                backtrack(path)
            
                # undo
                path.pop()

        backtrack([])
        return result
    
sol = Solution()
nums = [1, 2, 3]
result = sol.permute(nums)
print(result)
        
            
            
            