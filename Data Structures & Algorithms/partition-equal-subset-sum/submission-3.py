class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0

        for number in nums:
            total += number

        if total % 2 != 0:
            return False

        target = total // 2
        memo = {}

        def dfs(i, target):
            if target == 0:
                return True

            if i >= len(nums) or target < 0:
                return False

            if (i, target) in memo:
                return memo[(i, target)]

            # Take nums[i]
            take = dfs(i + 1, target - nums[i])

            # Don't take nums[i]
            skip = dfs(i + 1, target)

            memo[(i, target)] = take or skip

            return memo[(i, target)]

        return dfs(0, target)