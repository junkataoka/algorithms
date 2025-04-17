"""
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:

Input: n = 2

Output: 2
Explanation:

1 + 1 = 2
2 = 2
Example 2:

Input: n = 3

Output: 3
Explanation:

1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3
Constraints:

"""

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    dp1 = 1
    dp2 = 2
    for i in range(2, n):
        dp1, dp2 = dp2, dp1 + dp2
    return dp2
    
