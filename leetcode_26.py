"""
Docstring for leetcode_26
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and return the new length.
nums = [1,1,2]
→ nums becomes [1,2,_]
return 2
"""
"""
ALGORITHM

Get the array and check if its not empty
Get the number at the first index and compare it to the other numbers in the array
Remove if there is a match, and shrink the array
Check the next number and repeat step 2 and 3 until the end of the array
return the array
"""

num = [1,1,2,1,3,1]

def remove_duplicates(array):
    if len(array) == 0:
        return "This array is empty"
    else:
        for i in range(len(num)):
            for j in range(i, len(num)-1):
                if num[i] == num[j]:
                    num.pop(j)
                    
        return num
    
print(remove_duplicates(num))