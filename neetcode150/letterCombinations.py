"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Solution
1. create a hashmap to with keys(nums) and values(characters)
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
        
        letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, path):
            
            if index == len(digits):
                result.append(path)
                return
            
            current_digit = digits[index]
            for letter in letter_map[current_digit]:
                backtrack(index=index + 1, path=path + letter)
        
        backtrack(0, '')
        return result
        
digits = '2'
sol = Solution()
result = sol.letterCombinations(digits=digits)
print(result)
