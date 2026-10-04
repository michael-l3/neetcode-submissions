class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(currAmount):
            if currAmount == 0:
                return 0

            if currAmount < 0:
                return float("inf")

            if currAmount in memo:
                return memo[currAmount]

            smallest = float("inf")

            for coin in coins:
                result = dfs(currAmount - coin)
                smallest = min(smallest, result)

            memo[currAmount] = 1 + smallest

            return memo[currAmount]

        result = dfs(amount)

        if result == float("inf"):
            return -1

        return result