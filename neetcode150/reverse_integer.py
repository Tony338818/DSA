"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

def reverseInteger(num: int) -> int:
    MAX_RANGE = 2 ** 32 -1
    MIN_RANGE = -(2 ** 32)
    
    result = 0
    
    while num != 0:
        
        digit = num % 10 if num > 0 else -(abs(num) % 10)
        
        num = num // 10
        
        if result > MAX_RANGE // 10 or (result == MAX_RANGE // 10 and digit > 7):
            return 0
        if result < MIN_RANGE // 10 or (result == MIN_RANGE // 10 and digit < -8):
            return 0
        
        result = result * 10 + digit
        
    return result

num = 321
result = reverseInteger(321)
print(result)