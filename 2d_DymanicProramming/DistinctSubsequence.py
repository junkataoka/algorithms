"""
You are given two strings s and t, both consisting of english letters.

Return the number of distinct subsequences of s which are equal to t.

Example 1:

Input: s = "caaat", t = "cat"

Output: 3
Explanation: Rhere are 3 ways you can generate "cat" from s.

(c)aa(at)
(c)a(a)a(t)
(ca)aa(t)
Example 2:

Input: s = "xxyxy", t = "xy"

Output: 5
Explanation: There are 5 ways you can generate "xy" from s.

(x)x(y)xy
(x)xyx(y)
x(x)(y)xy
x(x)yx(y)
xxy(x)(y)
Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""

def numDistinct(s: str, t: str) -> int:

    memo = {}

    def dfs(i, j):

        if j == len(t):
            return 1
        
        if i == len(s):
            return 0
        
        if (i, j) in memo:
            return memo[(i, j)]
            
        count = 0

        if s[i] == t[j]:
            count += dfs(i+1, j+1)
        
        count += dfs(i+1, j)
        memo[(i, j)] = count
        
        return memo[(i, j)]
    
    return dfs(0, 0)

# Time complexity: O(n * m)
# Space complexity: O(n * m)

def numDistinct(s: str, t: str) -> int:
    m = len(s)
    n = len(t)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]



