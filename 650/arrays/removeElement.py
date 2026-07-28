"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

def removeElement(nums: list, val: int):
    """
    keep a k count that starts at 0, loop through the array, and check if the number there is not equal to 2, then we update
    nums[k] with that number and increase k.
    """
    k = 0
    
    for read in range(len(nums)):
        if nums[read] != val:
            nums[k] = nums[read]
            k += 1
    
    return k
    

nums = [0,1,2,2,3,0,4,2]
val = 2
result = removeElement(nums, val)
print(result)