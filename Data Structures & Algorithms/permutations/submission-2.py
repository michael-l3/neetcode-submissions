
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        level = []
        visited = set()

        def dfs():
            if len(level) == len(nums):
                res.append(level.copy())
                return

            for number in nums:
                if number in visited:
                    continue

                visited.add(number)
                level.append(number)

                dfs()

                # Backtrack
                level.pop()
                visited.remove(number)

        dfs()
        return res
