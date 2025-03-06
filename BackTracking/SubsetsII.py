"""
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]
Constraints:

1 <= nums.length <= 11
-20 <= nums[i] <= 20

"""

def subsetsWithDup(nums):
    res = []
    nums.sort()
    def backtrack(idx, path):
        if idx == len(nums):
            res.append(path)
            return
        path.append(nums[idx])
        backtrack(idx + 1, path[:])
        path.pop()
        while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
            idx += 1
        backtrack(idx + 1, path[:])
    backtrack(0, [])
    return res

