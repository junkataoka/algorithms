"""
Insert Interval
Solved 
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

Example 1:

Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

Output: [[1,6]]
Example 2:

Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

Output: [[1,2],[3,5],[6,7],[9,10]]
Constraints:

0 <= intervals.length <= 1000
newInterval.length == intervals[i].length == 2
0 <= start <= end <= 1000
"""

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    merged = []
    i = 0
    n = len(intervals)
    
    # Add all intervals before the new interval
    while i < n and intervals[i][1] < newInterval[0]:
        merged.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    merged.append(newInterval)
    
    # Add remaining intervals
    while i < n:
        merged.append(intervals[i])
        i += 1
    
    return merged
