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

    counter = [0] * 26
    max_len = 0
    max_count = 0
    left = 0

    for right in range(len(s)):
        counter[ord(s[right]) - ord('A')] += 1
        max_count = max(max_count, counter[ord(s[right]) - ord('A')])

        while right - left + 1 - max_count > k:
            counter[ord(s[left]) - ord('A')] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

