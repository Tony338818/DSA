"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

def subarraysum(nums, k):
    sub = 0
    current_sum = 0
    prefix = {0: 1}
    
    for num in nums:
        current_sum += num
        
        if current_sum - k in prefix:
            sub += prefix[current_sum - k]
            
        prefix[current_sum] = prefix.get(current_sum, 0) + 1
    
    return sub

nums = [1,2,3]
k = 2

result = subarraysum(nums=nums, k=k)
print(result)
        