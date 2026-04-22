"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


My process

Input -> Array and target
Output -> 2 indices == target

My Solution:
- Make use of two pointers, one slow and one fast pointer
steps:
- initialize both pointers second at index 0 and first at index 1
- compare the values everytime the first pointer moves
- if it gets to the end with no match the second pointer moves one step foward, and the first pointer starts in front of it
"""


def two_sum(arr, target):
    seen = {}
    
    for i, value in enumerate(arr):
        complement = target - value

        if complement in seen:
            return [seen[complement], i]

        seen[value] = i
        
arr = [1,2,3,4,5]
target = 9

result = two_sum(arr=arr, target=target)
print(result)