
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        level = []
        res = []

        def dfs(i, currSum):
            if currSum == target:
                res.append(level.copy())
                return

            if i >= len(candidates) or currSum > target:
                return

            # Take the current number
            level.append(candidates[i])
            dfs(i + 1, currSum + candidates[i])

            # Backtrack: remove the number we took
            level.pop()

            # Skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            # Skip the current number
            dfs(i + 1, currSum)

        dfs(0, 0)
        return res
