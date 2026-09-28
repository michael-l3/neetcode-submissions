class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [] 
        sol = [] 

        def dfs(openn, close): 
            if len(sol) == 2*n: 
                ans.append(''.join(sol))
                return 
            
            if openn < n: 
                #take open
                sol.append('(') 
                dfs(openn+1,close)

                #remove the open 
                sol.pop() 
            
            if openn > close: 
                #take close 
                sol.append(')')
                dfs(openn,close+1)
                sol.pop()
        
        dfs(0,0)
        return ans