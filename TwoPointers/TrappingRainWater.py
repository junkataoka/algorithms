"""
Trapping Rain Water
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:



Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
"""

def trap(height):
    l, r = 0, len(height)-1
    left_max, right_max = 0, 0
    res = 0

    while l < r:
        left_max = max(left_max, height[l])
        right_max = max(right_max, height[r])

        if left_max < right_max:
            res += left_max - height[l]
            l += 1
        else:
            res += right_max - height[r]
            r -= 1
    return res
