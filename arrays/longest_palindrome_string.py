"""
Given a string s, return the longest palindromic substring in s.
"""
def longestPalindrome(s):
    if not s:
        return ''
    
    start, end = 0, 0
    
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right -1
    
    for i in range(len(s)):
        # odd length palindrome
        l1, r1 = expand(i, i)
        # even length palindrome
        l2, r2 = expand(i, i+1)
        
        # Pick the longer one
        if r1 - l1 > end - start :
           start, end = l1, r1 
        if r2 - l2 > end - start :
           start, end = l2, r2
           
    return s[start: end + 1] 

s = "babad"
result = longestPalindrome(s)
print(result)