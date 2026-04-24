"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_capacity = 0
        
        while left < right:
            current_capacity = min(height[left], height[right]) * (right - left)
            max_capacity = max(max_capacity, current_capacity)
            
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right] :
                right -= 1
            else:
                left += 1
                
        return max_capacity
    
height = [1,1]
sol = Solution()
result = sol.maxArea(height=height)
print(result)