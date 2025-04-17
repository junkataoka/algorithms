"""
 def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        cache = {}

        def dfs(i, j):
            if j == n:
                return i == m
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            match = i < m and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < n and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j)))

                return cache[(i, j)]
            
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)

                return cache[(i, j)]

            
            cache[(i, j)] = False

            return False
        
        return dfs(0, 0)


"""

def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)

    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    for j in range(1, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = s[i - 1] == p[j - 1] or p[j - 1] == "."
            if match:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == "*":
                dp[i][j] = dp[i][j - 2] or (match and dp[i - 1][j])

    return dp[m][n]

# dfs solution


def isMatch(s: str, p: str) -> bool:

    m, n = len(s), len(p)

    cache = {}

    def dfs(i, j):
        if j == n:
            return i == m
        
        if (i, j) in cache:
            return cache[(i, j)]
        
        match = i < m and (s[i] == p[j] or p[j] == ".")

        if (j + 1) < n and p[j + 1] == "*":
            cache[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j)))

            return cache[(i, j)]
        
        if match:
            cache[(i, j)] = dfs(i + 1, j + 1)

            return cache[(i, j)]

        
        cache[(i, j)] = False

        return False
    
    return dfs(0, 0)


