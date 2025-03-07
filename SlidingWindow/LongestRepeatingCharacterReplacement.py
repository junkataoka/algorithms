"""
ou are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 1000
0 <= k <= s.length

"""

def characterRepleacement(s, k):
    count_freq = {}
    max_freq = 0
    res = 0
    l = 0
    for r in range(len(s)):
        count_freq[s[r]] = count_freq.get(s[r], 0) + 1
        max_freq = max(max_freq, count_freq[s[r]])
        cur_len = r - l + 1
        if cur_len - max_freq > k:
            count_freq[s[l]] -= 1
            l += 1

        res = max(res, r-l+1)
    return res
