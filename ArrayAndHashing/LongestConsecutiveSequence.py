"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""

def logestConsecutive(nums):
    if not nums:
        return 0

    nums = set(nums)
    max_len = 1

    for num in nums:
        if num - 1 not in nums:
            curr_num = num
            curr_len = 1

            while curr_num + 1 in nums:
                curr_num += 1
                curr_len += 1

            max_len = max(max_len, curr_len)

    return max_len
