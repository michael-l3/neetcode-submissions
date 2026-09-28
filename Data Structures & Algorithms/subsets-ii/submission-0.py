from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 1. MUST sort to group duplicates
        res = []

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return

            # 1. TAKE nums[i]
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()

            # 2. SKIP nums[i] (and step past all duplicate occurrences of nums[i])
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, curr)

        dfs(0, [])
        return res