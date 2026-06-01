"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        
        intervals = sorted(intervals)
        
        result.append(intervals[0])
        
        for i in range(1, len(intervals)):                
            if result[-1][-1] >= intervals[i][0]:
                result[i-1][-1] = max(result[i-1][-1], intervals[i][-1])
            else:
                result.append(intervals[i])
                
        return result
    
sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
result = sol.merge(intervals)
print(result)
