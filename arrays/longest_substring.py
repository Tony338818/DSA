"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

def lss(s):
    sub_string = set()
    left = 0
    max_length = 0

    for c in range(len(s)):
        while s[c] in sub_string:
            sub_string.remove(s[left])
            left += 1
        
        sub_string.add(s[c])
        max_length = max(max_length, c - left + 1)
    
    return max_length, sub_string

s = 'abcabcbb'
result = lss(s)
print(result)