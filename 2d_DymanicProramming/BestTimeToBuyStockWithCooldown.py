"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:

After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
You may only own at most one NeetCoin at a time.
You may complete as many transactions as you like.

Return the maximum profit you can achieve.

Example 1:

Input: prices = [1,3,4,0,4]

Output: 6
Explanation: Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. Total profit is 2 + 4 = 6.

Example 2:

Input: prices = [1]

Output: 0
Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000

"""

def maxProfit(prices: List[int]) -> int:

    dp = {} # key = (i, buying) val = max_profit

    def dfs(i, buying):
        if i >= len(prices):
            return 0
        
        if buying:
            buy = dfs(i + 1, buying=False) - prices[i]
            cooldown = dfs(i + 1, buying=True)
            dp[(i, buying)] = max(cooldown, buy)


        if not buying:
            sell = dfs(i+2, buying=True) + prices[i]
            cooldown = dfs(i + 1, buying=False)
            dp[(i, buying)] = max(cooldown, sell)

        return dp[(i, buying)]

    return dfs(0, True)

