"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
"""

"""
itype: list[int]
output: int
"""

def removeDuplicates(nums):
    """
    
    """
    if not nums: 
        return 0
    
    write = 1
    
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
            
    return write
    
nums = [0,0,1,1,1,2,2,3,3,4]
result = removeDuplicates(nums)
print(result)

"""
The Two Pointers Explainedread (The Explorer): Moves through the array one step at a time to examine each number.write (The Keeper): Tracks the position where the next unique number should be saved in nums.1.Initialize the Write Pointer:write = 1.We set write = 1 because nums[0] is already in its correct position as the first unique element. write is waiting at index 1 to receive the second unique element we discover.2.Scan with the Read Pointer:for read in range(1, len(nums)):.The read pointer loops through the array starting from index 1 all the way to the end.3.Check for a New Unique Element:if nums[read] != nums[read - 1]:.At each step, read compares the current number with the one immediately before it:If they are equal: It's a duplicate! Do nothing and let read move to the next number.If they are different: We found a brand-new unique value!4.Overwrite and Advance:nums[write] = nums[read] and write += 1.When a new unique element is found, we copy nums[read] into the position tracked by nums[write]. Then, we increment write += 1 so it's ready for the next unique value.
"""