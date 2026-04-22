"""
Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.
"""


def longest_substring_with_k(s, k):
    sub_string = set()
    ss = {}
    left = 0
    max_ = 0
    
    for right in range(len(s)):
        ss[s[right]] = ss.get(s[right],0) + 1
        
        while len(ss) > k:
            ss[s[left]] -= 1
            if ss[s[left]] == 0:
                del(ss[s[left]])
            left += 1
        max_ = max(max_, right - left + 1)
    
    return max_

s = 'eceba'
k = 2

result = longest_substring_with_k(s=s, k=k)
print(result)