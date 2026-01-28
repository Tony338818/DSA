"""
Docstring for longest_substring
Given a string s, find the length of the longest substring without duplicate characters.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s1 = set()
        left = 0
        length = 0
        
        for i in range(len(s)):
            while s[i] in s1:
                s1.remove(s[left])
                left += 1
            
            s1.add(s[i])
            length = max(length, i - left + 1)
        return length

s = "abcabcbb"
so = Solution()
print(so.lengthOfLongestSubstring(s))