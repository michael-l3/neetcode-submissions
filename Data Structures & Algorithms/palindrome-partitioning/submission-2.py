from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        sol = []

        # Two-pointer palindrome check ($O(1)$ extra space)
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(i: int):
            if i >= len(s):
                ans.append(sol.copy())
                return

            for j in range(i, len(s)):
                # Pass indices i and j directly to the two-pointer helper
                if is_palindrome(i, j):
                    sol.append(s[i : j + 1])  # 1. Take / Cut
                    dfs(j + 1)                 # 2. Recurse forward past j
                    sol.pop()                  # 3. Backtrack

        dfs(0)
        return ans