"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
itype: list[int], int
return: int, int
"""

def twoSum(nums: list, target: int):
    """
    create and initialize and empty hashmap.
    loop through the input list, and check for each the number we check if the target - number exists in the set.
    if it does not exist we store the number as key, and it's index as value, else we return the indices.
    """
    
    seen = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in seen:
            return seen[complement], i
        
        
        seen[nums[i]] = i
        
        

nums = [2,7,11,15]
target = 9
result = twoSum(nums, target)
print(result)
    

