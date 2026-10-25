
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        nums = candidates
        res = []
        level = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(level.copy())
                return

            if currSum > target or i >= len(nums):
                return

            # Take the number
            level.append(nums[i])
            dfs(i + 1, currSum + nums[i])
            level.pop()

            # Skip the number and all duplicates at this level
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1

            dfs(i + 1, currSum)

        dfs(0, 0)
        return res
