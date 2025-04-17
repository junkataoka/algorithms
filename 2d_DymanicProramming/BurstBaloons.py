"""
You are given an array of integers nums of size n. The ith element represents a balloon with an integer value of nums[i]. You must burst all of the balloons.

If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.

Return the maximum number of coins you can receive by bursting all of the balloons.

Example 1:

Input: nums = [4,2,3,7]

Output: 167

Explanation:
nums = [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []
coins =  4*2*3    +   4*3*7   +  1*4*7  + 1*7*1 = 143
Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""

def maxCoins(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    dp = {}


    def dfs(l, r):

        if l > r:
            return 0
        if (l, r) in dp:
            return dp[(l, r)]
        
        dp[(l, r)] = 0
        
        max_coins = 0

        for i in range(l, r+1):
            coins = nums[l-1] * nums[i] * nums[r+1]
            coins += dfs(l, i-1) + dfs(i+1, r)
            dp[(l, r)] = max(dp[(l, r)], coins)
        
        return dp[(l, r)]
    
    return dfs(1, len(nums) - 2)


# More easy to read version
def maxCoins(nums: List[int]) -> int:
    nums = [1] + nums + [1]  # Add boundary balloons
    n = len(nums)
    dp = [[0] * n for _ in range(n)]  # Initialize DP table
    
    for length in range(1, n - 1):  # Length of subarray
        for left in range(1, n - length):  # Left boundary
            right = left + length - 1  # Right boundary
            for i in range(left, right + 1):  # Last balloon to burst
                coins = nums[left - 1] * nums[i] * nums[right + 1]  # Coins from last burst
                coins += dp[left][i - 1] + dp[i + 1][right]  # Add coins from left and right subarrays
                dp[left][right] = max(dp[left][right], coins)  # Update maximum
    
    return dp[1][n - 2]  # Return result for the entire array
            


