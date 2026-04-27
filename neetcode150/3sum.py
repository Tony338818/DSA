"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Solution:
1) sort the incoming array in ascending order
2) loop through the array and for each position of i, use a two pointers technique to find j & k
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        values = []
        nums.sort()
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                elif total == 0:
                    values.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
        return values

nums = [-1,0,1,2,-1,-4]  
sol = Solution()
result = sol.threeSum(nums=nums)
print(result)