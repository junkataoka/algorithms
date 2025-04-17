"""
You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]

Output: true
Explanation: The array can be partitioned as [1, 4] and [2, 3].

Example 2:

Input: nums = [1,2,3,4,5]

Output: false
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 50

"""

def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

# Time complexity: O(n * sum(nums))
# Space complexity: O(sum(nums))

# Top-down approach
def canPartition(nums):

    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    dp = {}

    def dfs(i, target):
        if target == 0:
            return True
        if i == len(nums) or target < 0:
            return False

        if (i, target) in dp:
            return dp[(i, target)]

        dp[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
        return dp[(i, target)]

    return dfs(0, target)
