
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        level = []

        def dfs(o, c):
            if len(level) == 2 * n:
                res.append(''.join(level))
                return

            # Add an opening parenthesis
            if o < n:
                level.append("(")
                dfs(o + 1, c)
                level.pop()

            # Add a closing parenthesis
            if o > c:
                level.append(")")
                dfs(o, c + 1)
                level.pop()

        dfs(0, 0)
        return res
