"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

def longestSubstringWithoutRepeat(s):
    sub_string = set()
    max_length = 0
    l = 0
    
    for r in range(len(s)):
        while s[r] in sub_string:
            sub_string.remove(s[l])
            l += 1
        
        sub_string.add(s[r])
        max_length = max(max_length, r - l + 1)
        
    return max_length

s = "bbbb"
result = longestSubstringWithoutRepeat(s=s)
print(result)
