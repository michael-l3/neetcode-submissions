class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        p_set = set() 
        a_set = set() 

        #so we know the boarding edges can make it 
        for i in range(rows): 
            p_set.add((i,0))
            a_set.add((i,cols-1))
        
        for j in range(cols): 
            p_set.add((0,j))
            a_set.add((rows-1,j))
        
        #so now we have all of the points that can hit it 
        def dfs(r,c,visted,prevHeight):

            #check around 
            for i_off, j_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
                i = r + i_off
                j = c + j_off 

                if 0 <= i < rows and 0 <= j < cols and (i,j) not in visted and heights[i][j] >= prevHeight: 
                    visted.add((i,j))
                    dfs(i,j,visted,heights[i][j]) 
        
        #row function  
        for r in range(rows): 
            dfs(r,0,p_set,heights[r][0])
            dfs(r,cols-1,a_set,heights[r][cols-1])
        
        #column function 
        for c in range(cols): 
            dfs(0,c,p_set,heights[0][c])
            dfs(rows-1,c,a_set,heights[rows-1][c])
              
        

        res = []
        for i in range(rows): 
            for j in range(cols): 
                if (i,j) in a_set and (i,j) in p_set: 
                    res.append([i,j])
        
        return res 