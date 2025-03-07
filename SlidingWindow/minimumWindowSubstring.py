"""
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
"""
import collections

def minWindow(s: str, t: str) -> str:
    t_count = collections.Counter(t)
    window_count = {}
    l = 0
    need = len(t_count)
    have = 0
    min_len = float("inf")
    res = [-1, -1]

    for r in range(len(s)):

        window_count[s[r]] = window_count.get(s[r], 0) + 1
        if window_count[s[r]] == t_count[s[r]]:
            have += 1
        
        while have == need:
            cur_len = r - l + 1
            if min_len > cur_len:
                min_len = cur_len
                res = [l, r]
            
            window_count[s[l]] -= 1
            if window_count[s[l]] < t_count[s[l]]:
                have -= 1
            l += 1
    
    return s[res[0]:res[1]+1] if min_len < float("inf") else ""


