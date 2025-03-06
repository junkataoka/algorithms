"""
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [7]

Output: [[],[7]]
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

def subsets(nums):
    res = []
    def backtrack(idx, path):
        if idx == len(nums):
            res.append(path)
            return
        backtrack(idx + 1, path + [nums[idx]])
        backtrack(idx + 1, path)
    backtrack(0, [])
    return res


