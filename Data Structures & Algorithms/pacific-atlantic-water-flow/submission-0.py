class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #we want to capture two sets: ones that can get to pacific and ones that can get to atlantic 
        m = len(heights) # -> rows 
        n = len(heights[0]) #-> columns 
        a_set = set()
        p_set = set()

        def dfs(row, column, visted, prevHeight): 
            #base case to not append
            if row < 0 or row >= m or column < 0 or column >= n or (row,column) in visted or heights[row][column] < prevHeight: 
                return  
            
            # add the valid point to the list
            visted.add((row,column))

            #now checke the neighboring cells 
            for r_off, c_off in [(1,0),(-1,0),(0,-1),(0,1)]: 
                rx = row + r_off 
                cx = column + c_off 

                dfs(rx,cx,visted,heights[row][column])

        #so for all of the rows we need to have the  left and right side
        for r in range(m): 
            #we will have to dfs and give the points, prevHeight bc we can only come from higher Heights  
            dfs(r,0,p_set,heights[r][0])
            dfs(r,n-1,a_set,heights[r][n-1]) 

        #for all columns we need top and bottom
        for c in range(n): 
            dfs(0,c,p_set,heights[0][c])
            dfs(m-1,c,a_set,heights[m-1][c])
        
        res = []
        #now p_set and a_set should be filled out 
        #find the intersection
        for i in range(m): 
            for j in range(n): 
                if (i,j) in p_set and (i,j) in a_set: 
                    res.append([i,j])
        
        return res

        
