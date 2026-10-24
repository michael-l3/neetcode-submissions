class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #so for 2d dynamic programming we will build out a memoization jusat like we did in 1D 
        #since we arent explictly given a grid we have to build it out and it will be our answer 
        #memo is an array in 2d dynamic programming
        memo = []
        for r in range(m): 
            row = [] 
            for c in range(n): 
                row.append(-1)
            memo.append(row)
    
        #now we have something like this 
        #[-1,-1,-1]
        #[-1,-1,-1]
        #[-1,-1,-1] 

        def dp(r,c): 
            #our first base case is if it is out of bounds 
            if r >= m or c >= n: 
                return 0 
            
            #we hit our base case where we hit the target 
            if r == (m-1) and c == (n-1): 
                return 1 
            
            #we also need to see if where we are is in the memo 
            value = memo[r][c]
            if value != -1: 
                return value
            
            goingDown = dp(r+1,c)
            goingRight = dp(r,c+1)
            total = goingDown + goingRight

            memo[r][c] = total 
            return memo[r][c]
        
        return dp(0,0)
