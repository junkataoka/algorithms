"""
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:

Input: n = 00000000000000000000000000010111

Output: 4
Example 2:

Input: n = 01111111111111111111111111111101

Output: 30

"""

def hammingWeight(n: int) -> int:
    count = 0
    while n > 0:
        count += n & 1  # Increment count if the last bit is 1
        n >>= 1         # Right shift n by 1 to check the next bit
    return count
