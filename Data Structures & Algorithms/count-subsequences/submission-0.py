class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        
        # 1. Size the memo board with + 1 for out-of-bounds safety
        memo = [] 
        for i in range(m): 
            row = [] 
            for j in range(n): 
                row.append(-1)
            memo.append(row)
        
        def dfs(si, ti): 
            # Base Case 1: If we successfully matched every character in t, we found 1 valid subsequence!
            if ti == len(t): 
                return 1
            
            # Base Case 2: If we ran out of characters in s but still need characters in t, 0 ways.
            if si == len(s):
                return 0
            
            # Memo check
            if memo[si][ti] != -1: 
                return memo[si][ti] 
            
            solution = 0 
            
            # If the current characters match, we have TWO choices:
            # Choice A: Use the match (advance both)
            # Choice B: Skip the character in s (advance only si)
            if s[si] == t[ti]: 
                solution += dfs(si + 1, ti + 1) + dfs(si + 1, ti)
            else: 
                # If they don't match, we MUST skip the character in s
                solution += dfs(si + 1, ti)
            
            memo[si][ti] = solution 
            return memo[si][ti]
          
        return dfs(0, 0)