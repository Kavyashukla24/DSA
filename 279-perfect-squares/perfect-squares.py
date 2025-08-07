class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        coins=[]
        i = 1
        while i * i <= n:
            coins.append(i * i)
            i += 1
        for coin in coins:
            for x in range(coin, n + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[n] if dp[n] != float('inf') else -1


        