"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # base case
        if n == 0:
            return 1
        
        # negative case
        if n < 0:
            return self.myPow(1/x, -n)
        
        if n % 2 == 0:
            return self.myPow(x, n // 2) * self.myPow(x, n//2)
        else:
            return self.myPow(x, n // 2) * self.myPow(x, n // 2) * x


sol = Solution()
x = 2.0000
n = -2
print(sol.myPow(x, n))
