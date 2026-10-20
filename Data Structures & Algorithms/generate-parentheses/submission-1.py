class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #so the rules for this is that open must be what we are looking for because 
        #close can never be greater than open 
        res = [] 
        level = [] 

        def dfs(close,openn): 
            if len(level) == 2 * n: 
                res.append(''.join(level))
                return 
            
            #we need to prioritize opens 
            if openn < n: 
                #take opens 
                level.append('(')
                dfs(close,openn + 1)
            
                #remove 
                level.pop() 

            if openn > close: 
                level.append(')')
                dfs(close + 1, openn)
                level.pop()

        
        dfs(0,0)
        return res