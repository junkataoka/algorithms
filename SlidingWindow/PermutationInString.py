"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000
"""

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_count = [0] * 26
    window_count = [0] * 26

    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord("a")] += 1
        window_count[ord(s2[i]) - ord("a")] += 1

    if s1_count == window_count:
        return True
    
    for r in range(len(s1), len(s2)):
        window_count[ord(s2[r]) - ord("a")] += 1
        window_count[ord(s2[r - len(s1)]) - ord("a")] -= 1
        if s1_count == window_count:
            return True

    return False


    
