"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):
    seen = {}
    
    for i, v in enumerate(nums):
        complement = target - v
        print(seen)
        
        if complement in seen:
            return seen[complement], i
        
        seen[v] = i
        
nums = [2,7,11,15]
target = 22
result = twoSum(nums=nums, target=target)
print(result)