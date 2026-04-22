"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums 
except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

"""
Input = int[1, 2, 3, 4]
Expected Output = [24, 12, 8, 6]
constraint = must run in O(n) without using division operation
"""
import math

# My Brute Force
def productExceptSelfBrute(nums):
    array = []
    
    for i in range(len(nums)):
        left = nums[:i]
        right = nums[i+1:]
        
        array.append(math.prod(left) * math.prod(right))
    
    return array

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # prefix
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
        
    print(result)    
    
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
        
    return result

nums = [1,2,3,4]
result = productExceptSelf(nums=nums)
print(result)