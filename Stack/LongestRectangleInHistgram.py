"""
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8
Example 2:

Input: heights = [1,3,7]

Output: 7
Constraints:

1 <= heights.length <= 1000.
0 <= heights[i] <= 1000

"""

def largestRectrangle(heights):
    max_area = 0

    stack = [] 

    for i, height in enumerate(heights):
        start = i

        while stack and stack[-1][1] > height:
            prev_i, prev_h = stack.pop()
            width = i - prev_i
            area = prev_h * width
            max_area = max(max_area, area)
            start = prev_i
        
        stack.append((start, height))
    
    for i, height in stack:
        width = len(heights) - i
        area = height * width
        max_area = max(max_area, area)
    
    return max_area



