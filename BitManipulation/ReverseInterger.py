"""
You are given a signed 32-bit integer x.

Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

Solve the problem without using integers that are outside the signed 32-bit integer range.

Example 1:

Input: x = 1234

Output: 4321
Example 2:

Input: x = -1234

Output: -4321
Example 3:

Input: x = 1234236467

Output: 0
Constraints:

-2^31 <= x <= 2^31 - 1
"""
# Bit Manipulation Solution
def reverse(x):
    sign = 1
    if x < 0:
        sign = -1
        x = -x
    
    result = 0
    while x != 0:
        digit = x % 10
        x //= 10
        
        # Check for overflow
        if (result > (2**31 - 1) // 10) or (result == (2**31 - 1) // 10 and digit > 7):
            return 0
        
        result = result * 10 + digit
    
    return sign * result

