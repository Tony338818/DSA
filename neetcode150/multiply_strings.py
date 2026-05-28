"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 =="0":
            return "0"
        
        m,n = len(num1), len(num2)
        result = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                
                # Convert characters to single-digit integers
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')
                
                # Multiply the digits
                mul = d1 * d2
                
                # Determine the two positions in the array affected by this multiplication
                p1 = i + j
                p2 = i + j + 1
                
                # Add the product to the current value at position p2
                total_sum = mul + result[p2]
                
                # Update the array with the remainder and the carry
                result[p2] = total_sum % 10
                result[p1] = total_sum // 10
                
        start_idx = 0
        while start_idx < len(result) and result[start_idx] == 0:
            start_idx += 1
        
        return "".join(map(str, result[start_idx:]))
        
        
                
            
            
sol = Solution()
num1 = "2"
num2 = "3"
result = sol.multiply(num1, num2)
print(result)