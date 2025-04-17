"""
Partition Labels
You are given a string s consisting of lowercase english letters.

We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

Return a list of integers representing the size of these substrings in the order they appear in the string.

Example 1:

Input: s = "xyxxyzbzbbisl"

Output: [5, 5, 1, 1, 1]
Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].

Example 2:

Input: s = "abcabc"

Output: [6]
Constraints:

1 <= s.length <= 100
"""


from collections import defaultdict
from typing import List

def partitionLabels(s: str) -> List[int]:
    last_occurrence = {char: i for i, char in enumerate(s)}
    partitions = []
    end = 0
    size = 0

    for i, char in enumerate(s):
        end = max(end, last_occurrence[char])
        size += 1

        if i == end:
            partitions.append(size)
            size = 0

    return partitions
