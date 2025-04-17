"""
Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:

Input: a = 1, b = 1

Output: 2
Example 2:

Input: a = 4, b = 7

Output: 11
Constraints:

-1000 <= a, b <= 1000
"""


def getSum(a: int, b: int) -> int:
    while b != 0:
        carry = a & b  # carry now contains common set bits of a and b
        a = a ^ b  # Sum of bits of a and b where at least one of the bits is not set
        b = carry << 1  # Carry is shifted by one so that adding it to a gives the required sum
    return a
