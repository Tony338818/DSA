"""
Docstring for two_sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# O(n^2) not very efficient
def twosum(nums: list, target: int):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
            



def optimized_two_sum(nums: list, target:int):
    seen = {}
    
    for index, val in enumerate(nums):
        comp = target - val
        
        if comp in seen:
            return [seen[comp], index]
        seen[val] = index
        
        
        
nums = [1,2,3,4,5,6,7]
target = 8

print(twosum(nums, target))
print(optimized_two_sum(nums, target))

