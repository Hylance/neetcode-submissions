class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[j] = 使用目前已经考虑过的硬币面额，凑出金额 j 的组合数量。
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]
        