"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        max_sum = nums[0]
        
        for num in nums[1:]:
            if current_sum < 0:
                current_sum = num
                max_sum = max(max_sum, current_sum)
            else:
                current_sum += num
                max_sum = max(max_sum, current_sum)
                
            # alternatively
            # current_sum = max(num, current_sum + num)
            # max_sum = max(max_sum, current_sum)
            
        return max_sum
    
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
result = sol.maxSubArray(nums)
print(result)