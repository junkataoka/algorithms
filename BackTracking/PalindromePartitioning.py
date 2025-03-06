"""
Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:

Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"

Output: [["a"]]
Constraints:

1 <= s.length <= 20
s contains only lowercase English letters.

"""

def partition(s):
    res = []
    def is_palindrome(s):
        return s == s[::-1]
    def backtrack(start, path):
        if start == len(s):
            res.append(path)
            return

        for i in range(start, len(s)):
            if is_palindrome(s[start:i + 1]):
                backtrack(i + 1, path + [s[start:i + 1]])

    backtrack(0, [])
    return res
