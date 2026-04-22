"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
def median_of_sorted_arrays(arr1, arr2):
    arr1 += arr2
    arr1.sort()
    
    if len(arr1) % 2 == 0:
        mid_1 = (len(arr1)  // 2) - 1
        mid_2 = (len(arr1)  // 2)
        
        median = arr1[mid_1] + arr1[mid_2] / 2
    else :
        mid_1 = (len(arr1) // 2)
        median = arr1[mid_1]
    
    return median
        
        
nums1 = [1,3]
nums2 = [2]

result = median_of_sorted_arrays(nums1, nums2)
print(result)