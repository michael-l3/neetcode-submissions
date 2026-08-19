class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights) # -> #of rows
        n = len(heights[0]) # -> #of columns 
        p_set = set() 
        a_set = set()

        #iterate through the edges that are already boarding the grid we need to keep track of places 
        #that can be hit to the atlantic and those that can be hit from pac 
        #need a functions that recursively goes through and checks 

        def dfs(r,c,visted,prevHeight): 
            if r < 0 or r >= m or c < 0 or c >= n or (r,c) in visted or prevHeight > heights[r][c]: 
                return 

            visted.add((r,c))

            for r_off,c_off in [(1,0),(-1,0),(0,1),(0,-1)]: 
                rx = r + r_off 
                cx = c + c_off 

                dfs(rx,cx,visted,heights[r][c]) 
            
        #iterate to use function the rows 
        for r in range(m): 
            dfs(r,0,p_set,heights[r][0])
            dfs(r,n-1,a_set,heights[r][n-1]) 
        
        #column function
        for c in range(n): 
            dfs(0,c,p_set,heights[0][c])
            dfs(m-1,c,a_set,heights[m-1][c]) 

        res = [] 

        for i in range(m): 
            for j in range(n): 
                if (i,j) in a_set and (i,j) in p_set: 
                    res.append([i,j])
        
        return res
