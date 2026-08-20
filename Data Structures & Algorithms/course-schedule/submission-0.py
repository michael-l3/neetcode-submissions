class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        courses = prerequisites
        #create the graph 
        g = {} 
        #put nodes in graph 
        for a,b in courses: 
            if a not in g: 
                g[a] = []
            g[a].append(b)
        
        #now we have to have states of visting or not because we are trying to detect cycle 
        UNVISTED = 0 
        VISTING = 1 
        VISTED = 2 
        states = [UNVISTED] * numCourses 

        #now we must traverse through each node and check if that point is visted or not 
        def dfs(node): 
            #node will basically just be a number 
            state = states[node]  

            if state == VISTED: 
                return True 
            elif state == VISTING: 
                return False 
            
            #now we are change the nodes value if it isnt either to visiting 
            states[node] = VISTING 

            #check the neighbors of the node now 
            for nei in g.get(node,[]): 
                if not dfs(nei): 
                    return False 
            
            #now we cleared all the cases for the neighbor so we are visted 
            states[node] = VISTED 
            return True 
        
        #we will now iterate through each point 
        for i in range(numCourses): 
            if not dfs(i): 
                return False 
        
        return True