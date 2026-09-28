from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Create the memoization cache manually
        memo = {}

        def dfs(i: int) -> bool:
            # Base Case: Reached or surpassed the last index
            if i >= len(nums) - 1:
                return True

            # 1. Check if we already computed this index
            if i in memo:
                return memo[i]

            # Try all possible jumps from index i
            max_jump = min(i + nums[i], len(nums) - 1)
            for next_i in range(i + 1, max_jump + 1):
                if dfs(next_i):
                    memo[i] = True  # Cache positive result
                    return True

            # 2. If no jump worked, cache False and return
            memo[i] = False
            return False

        return dfs(0)