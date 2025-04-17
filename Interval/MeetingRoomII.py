"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000

"""

class Interval:
    def __init__(self, start: int = 0, end: int = 0):
        self.start = start
        self.end = end

from typing import List

def minMeetingRooms(intervals: List[Interval]) -> int:
    start = sorted([interval.start for interval in intervals])
    end = sorted([interval.end for interval in intervals])
    count = 0
    max_count = 0
    i = j = 0

    while i < len(start) and j < len(end):
        if start[i] >= end[j]:
            j += 1
            count -= 1
        
        elif start[i] < end[j]:
            count += 1
            i += 1
        
        max_count = max(count, max_count)
    
    return max_count
